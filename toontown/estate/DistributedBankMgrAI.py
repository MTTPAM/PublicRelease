#Embedded file name: toontown.estate.DistributedBankMgrAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedBankMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankMgrAI')

    def transferMoney(self, todo0):
        pass
