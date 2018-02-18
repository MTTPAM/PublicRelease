#Embedded file name: toontown.distributed.ToontownDistrictAI
import time
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.distributed.DistributedDistrictAI import DistributedDistrictAI

class ToontownDistrictAI(DistributedDistrictAI):
    notify = directNotify.newCategory('ToontownDistrictAI')

    def __init__(self, air):
        DistributedDistrictAI.__init__(self, air)
        self.created = 0
        self.ahnnLog = 0

    def announceGenerate(self):
        DistributedDistrictAI.announceGenerate(self)
        self.created = int(time.time())
        self.air.netMessenger.accept('queryShardStatus', self, self.handleShardStatusQuery)
        status = {'available': bool(self.available),
         'name': self.name,
         'created': int(time.time())}
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, status])
        status = {'available': False}
        datagram = self.air.netMessenger.prepare('shardStatus', [self.air.ourChannel, status])
        self.air.addPostRemove(datagram)

    def handleShardStatusQuery(self):
        status = {'available': bool(self.available),
         'name': self.name,
         'created': int(time.time())}
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, status])

    def allowAHNNLog(self, ahnnLog):
        self.ahnnLog = ahnnLog

    def d_allowAHNNLog(self, ahnnLog):
        self.sendUpdate('allowAHNNLog', [ahnnLog])

    def b_allowAHNNLog(self, ahnnLog):
        self.allowAHNNLog(ahnnLog)
        self.d_allowAHNNLog(ahnnLog)

    def getAllowAHNNLog(self):
        return self.ahnnLog

    def recordSuspiciousEventData(self, eventData):
        self.notify.warning(str(eventData))

    def setName(self, name):
        DistributedDistrictAI.setName(self, name)
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, {'name': name}])

    def setAvailable(self, available):
        DistributedDistrictAI.setAvailable(self, available)
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, {'available': bool(available)}])
