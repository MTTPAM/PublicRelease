#Embedded file name: toontown.shtiker.DeleteManagerAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DeleteManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DeleteManagerAI')

    def setInventory(self, todo0):
        pass
