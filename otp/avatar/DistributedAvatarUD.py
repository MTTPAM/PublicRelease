#Embedded file name: otp.avatar.DistributedAvatarUD
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedAvatarUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAvatarUD')

    def __init__(self, air):
        DistributedObjectUD.__init__(self, air)

    def setName(self, todo0):
        pass

    def setToonTag(self, tag):
        pass

    def friendsNotify(self, todo0, todo1):
        pass

    def checkAvOnShard(self, todo0):
        pass

    def confirmAvOnShard(self, todo0, todo1):
        pass
