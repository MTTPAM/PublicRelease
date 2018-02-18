#Embedded file name: toontown.rpc.ToontownRPCServer
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.stdpy import threading
import errno
from panda3d.core import TP_normal
import select
import socket
import urlparse
from toontown.rpc.ToontownRPCConnection import ToontownRPCConnection

class ToontownRPCServer:
    notify = directNotify.newCategory('ToontownRPCServer')

    def __init__(self, endpoint, handler):
        self.handler = handler
        url = urlparse.urlparse(endpoint)
        if url.scheme != 'http':
            self.notify.warning('Invalid scheme for endpoint: ' + str(url.scheme))
        self.hostname = url.hostname or 'localhost'
        self.port = url.port or 8080
        self.listenerSocket = None
        self.connections = {}
        self.dispatchThreads = {}

    def getUniqueName(self):
        return 'ToontownRPCServer-' + str(id(self))

    def start(self, useTaskChain = False):
        taskChain = None
        if useTaskChain and not taskMgr.hasTaskChain('ToontownRPCServer'):
            taskChain = 'ToontownRPCServer'
            taskMgr.setupTaskChain(taskChain, numThreads=1, threadPriority=TP_normal)
        self.listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listenerSocket.setblocking(0)
        self.listenerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listenerSocket.bind((self.hostname, self.port))
        self.listenerSocket.listen(5)
        taskName = self.getUniqueName() + '-pollTask'
        taskMgr.add(self.pollTask, taskName, taskChain=taskChain)

    def stop(self):
        taskName = self.getUniqueName() + '-pollTask'
        taskMgr.remove(taskName)
        for k, v in self.connections.items():
            v.close()
            del self.connections[k]

        try:
            self.listenerSocket.shutdown(socket.SHUT_RDWR)
        except socket.error:
            pass

        self.listenerSocket.close()
        self.listenerSocket = None

    def dispatchThread(self, socket):
        connection = self.connections[socket]
        connection.dispatchUntilEmpty()
        connection.close()
        del self.connections[socket]
        del self.dispatchThreads[socket]

    def pollOnce(self):
        try:
            rlist = select.select([self.listenerSocket] + self.connections.keys(), [], [])[0]
        except:
            try:
                self.listenerSocket.fileno()
            except:
                self.notify.error('The listener socket is no longer valid!')

            for socket in self.connections.keys():
                try:
                    socket.fileno()
                    socket.getpeername()
                except:
                    del self.connections[socket]
                    if socket in self.dispatchThreads:
                        del self.dispatchThreads[socket]

            return

        if self.listenerSocket in rlist:
            self.handleNewConnection()
        for socket in rlist:
            connection = self.connections.get(socket)
            if connection is None:
                continue
            if socket in self.dispatchThreads:
                continue
            self.dispatchThreads[socket] = threading.Thread(target=self.dispatchThread, args=[socket])
            self.dispatchThreads[socket].start()

    def pollTask(self, task):
        self.pollOnce()
        return task.cont

    def handleNewConnection(self):
        try:
            conn = self.listenerSocket.accept()[0]
        except socket.error as e:
            if e.args[0] != errno.EWOULDBLOCK:
                raise e

        self.connections[conn] = ToontownRPCConnection(conn, self.handler)
