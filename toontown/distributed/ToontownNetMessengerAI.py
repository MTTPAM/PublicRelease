#Embedded file name: toontown.distributed.ToontownNetMessengerAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
import cPickle, zlib

class ToontownNetMessengerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownNetMessengerAI')

    def __init__(self, air, msgChannel = 40000, msgType = 54321):
        self.air = air
        self.air.registerForChannel(msgChannel)
        self.msgChannel = msgChannel
        self.msgType = msgType

    def prepare(self, message, sentArgs = []):
        dg = PyDatagram()
        dg.addServerHeader(self.msgChannel, self.air.ourChannel, self.msgType)
        dg.addString(message)
        dg.addString(zlib.compress(cPickle.dumps(sentArgs)))
        return dg

    def send(self, message, sentArgs = []):
        self.notify.debug('sendNetEvent: %s %r' % (message, sentArgs))
        dg = self.prepare(message, sentArgs)
        self.air.send(dg)

    def handle(self, msgType, di):
        message = di.getString()
        data = zlib.decompress(di.getString())
        sentArgs = cPickle.loads(data)
        messenger.send(message, sentArgs)
