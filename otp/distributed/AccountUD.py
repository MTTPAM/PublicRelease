#Embedded file name: otp.distributed.AccountUD
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class AccountUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountUD')
    pirateAvatars = [0,
     0,
     0,
     0,
     0,
     0]

    def __init__(self, air):
        DistributedObjectUD.__init__(self, air)

    def setPirate(self, slot, avatarId):
        self.pirateAvatars[slot] = avatarId
        self.sendUpdate('pirateAvatars', self.pirateAvatars)

    def getPirate(self, slot):
        return self.pirateAvatars[slot]

    def getSlotLimit(self):
        return 6

    def may(self, perm):
        return 1
