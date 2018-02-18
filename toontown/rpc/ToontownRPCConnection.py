#Embedded file name: toontown.rpc.ToontownRPCConnection
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.stdpy import threading
from direct.stdpy import threading2
import httplib
import json
import socket
import time
from toontown.rpc.ToontownRPCDispatcher import ToontownRPCDispatcher

class ToontownRPCConnection():
    notify = directNotify.newCategory('ToontownRPCConnection')

    def __init__(self, socket, handler):
        self.socket = socket
        self.dispatcher = ToontownRPCDispatcher(handler)
        self.socketLock = threading.Lock()
        self.readLock = threading.RLock()
        self.writeLock = threading.RLock()
        self.readBuffer = ''
        self.writeQueue = []
        self.writeSemaphore = threading.Semaphore(0)
        self.writeThread = threading.Thread(target=self.__writeThread)
        self.writeThread.start()

    def __readHeaders(self):
        self.readLock.acquire()
        while '\r\n\r\n' not in self.readBuffer:
            try:
                self.readBuffer += self.socket.recv(2048)
            except:
                self.readLock.release()
                return {}

            if not self.readBuffer:
                self.readLock.release()
                return {}

        terminatorIndex = self.readBuffer.find('\r\n\r\n')
        data = self.readBuffer[:terminatorIndex]
        self.readBuffer = self.readBuffer[terminatorIndex + 4:]
        self.readLock.release()
        return self.__parseHeaders(data)

    def __parseHeaders(self, data):
        headers = {}
        for i, line in enumerate(data.split('\n')):
            line = line.rstrip('\r')
            if i == 0:
                words = line.split(' ')
                if len(words) != 3:
                    self.writeHTTPError(400)
                    return {}
                command, _, version = words
                if command != 'POST':
                    self.writeHTTPError(501)
                    return {}
                if version not in ('HTTP/1.0', 'HTTP/1.1'):
                    self.writeHTTPError(505)
                    return {}
            else:
                words = line.split(': ', 1)
                if len(words) != 2:
                    self.writeHTTPError(400)
                    return {}
                headers[words[0].lower()] = words[1]

        return headers

    def read(self, timeout = None):
        self.socketLock.acquire()
        self.socket.settimeout(timeout)
        headers = self.__readHeaders()
        if not headers:
            self.socketLock.release()
            return ''
        contentLength = headers.get('content-length', '')
        if not contentLength or not contentLength.isdigit():
            self.socketLock.release()
            self.writeHTTPError(400)
            return ''
        self.readLock.acquire()
        contentLength = int(contentLength)
        while len(self.readBuffer) < contentLength:
            try:
                self.readBuffer += self.socket.recv(2048)
            except:
                self.readLock.release()
                self.socketLock.release()
                return ''

            if not self.readBuffer:
                self.readLock.release()
                self.socketLock.release()
                return ''

        data = self.readBuffer[:contentLength]
        self.readBuffer = self.readBuffer[contentLength + 1:]
        self.readLock.release()
        self.socketLock.release()
        try:
            return data.decode('utf-8')
        except UnicodeDecodeError:
            return ''

    def __writeNow(self, data, timeout = None):
        self.writeLock.acquire()
        self.socket.settimeout(timeout)
        if not data.endswith('\n'):
            data += '\n'
        while data:
            try:
                sent = self.socket.send(data)
            except:
                break

            if sent == 0:
                break
            data = data[sent:]

        self.writeLock.release()

    def __writeThread(self):
        while True:
            self.writeSemaphore.acquire()
            if not self.writeQueue:
                continue
            request = self.writeQueue.pop(0)
            terminate = request.get('terminate')
            if terminate is not None:
                self.writeQueue = []
                terminate.set()
                break
            data = request.get('data')
            if data:
                self.__writeNow(data, timeout=request.get('timeout'))

    def write(self, data, timeout = None):
        self.writeQueue.append({'data': data,
         'timeout': timeout})
        self.writeSemaphore.release()

    def writeHTTPResponse(self, body, contentType = None, code = 200):
        response = 'HTTP/1.1 %d %s\r\n' % (code, httplib.responses.get(code))
        response += 'Date: %s\r\n' % time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        response += 'Server: TTI-RPCServer/0.1\r\n'
        response += 'Content-Length: %d\r\n' % len(body)
        if contentType is not None:
            response += 'Content-Type: %s\r\n' % contentType
        response += '\r\n' + body
        self.write(response, timeout=5)

    def writeHTTPError(self, code):
        self.notify.warning('Received a bad HTTP request: ' + str(code))
        body = '%d %s' % (code, httplib.responses.get(code))
        self.writeHTTPResponse(body, contentType='text/plain', code=code)

    def writeJSONResponse(self, response, id = None):
        response.update({'jsonrpc': '2.0',
         'id': id})
        try:
            body = json.dumps(response, encoding='latin-1')
        except TypeError:
            self.writeJSONError(-32603, 'Internal error')
            return

        self.writeHTTPResponse(body, contentType='application/json')

    def writeJSONError(self, code, message, id = None):
        self.notify.warning('Received a bad JSON request: %d %s' % (code, message))
        response = {'error': {'code': code,
                   'message': message}}
        self.writeJSONResponse(response, id=id)

    def close(self):
        terminate = threading2.Event()
        self.writeQueue.append({'terminate': terminate})
        self.writeSemaphore.release()
        terminate.wait()
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except socket.error:
            pass

        self.socket.close()

    def dispatchUntilEmpty(self):
        while True:
            data = self.read(timeout=5)
            if not data:
                break
            try:
                request = json.loads(data)
            except ValueError:
                self.writeJSONError(-32700, 'Parse error')
                continue

            request = ToontownRPCRequest(self, request.get('method'), params=request.get('params') or (), id=request.get('id'), notification='id' not in request)
            self.dispatcher.dispatch(request)


class ToontownRPCRequest():

    def __init__(self, connection, method, params = (), id = None, notification = False):
        self.connection = connection
        self.method = method
        self.params = params
        self.id = id
        self.notification = notification

    def result(self, result):
        if not self.notification:
            self.connection.writeJSONResponse({'result': result}, id=self.id)

    def error(self, code, message):
        if not self.notification:
            self.connection.writeJSONError(code, message, id=self.id)
