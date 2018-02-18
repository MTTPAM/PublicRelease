#Embedded file name: otp.distributed.AccountAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class AccountAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountAI')
    pirateAvatars = [0,
     0,
     0,
     0,
     0,
     0]

    def setPirate(self, slot, avatarId):
        pass

    def getPirate(self, slot):
        return self.pirateAvatars[slot]

    def getSlotLimit(self):
        return 6

    def may(self, perm):
        return 1
