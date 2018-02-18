#Embedded file name: toontown.distributed.ToontownInternalRepository
from direct.distributed.AstronInternalRepository import AstronInternalRepository
from otp.distributed.OtpDoGlobals import *
from toontown.distributed.ToontownNetMessengerAI import ToontownNetMessengerAI

class ToontownInternalRepository(AstronInternalRepository):
    GameGlobalsId = OTP_DO_ID_TOONTOWN
    dbId = 4003

    def __init__(self, baseChannel, serverId = None, dcFileNames = None, dcSuffix = 'AI', connectMethod = None, threadedNet = None):
        AstronInternalRepository.__init__(self, baseChannel, serverId=serverId, dcFileNames=dcFileNames, dcSuffix=dcSuffix, connectMethod=connectMethod, threadedNet=threadedNet)
        self.netMessenger.register(0, 'shardStatus')
        self.netMessenger.register(1, 'queryShardStatus')
        self.netMessenger.register(2, 'startInvasion')
        self.netMessenger.register(3, 'stopInvasion')
        self.__messenger = ToontownNetMessengerAI(self)

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 4294967295L

    def getAccountIdFromSender(self):
        return self.getMsgSender() >> 32 & 4294967295L

    def _isValidPlayerLocation(self, parentId, zoneId):
        if zoneId < 1000 and zoneId != 1:
            return False
        return True

    def sendNetEvent(self, message, sentArgs = []):
        self.__messenger.send(message, sentArgs)
