#Embedded file name: toontown.suit.SuitInvasionManagerAI
import time
from toontown.battle import SuitBattleGlobals
from toontown.suit import SuitDNA
from toontown.suit.SuitInvasionGlobals import *
from toontown.toonbase import ToontownGlobals

class SuitInvasionManagerAI:

    def __init__(self, air):
        self.air = air
        self.invading = False
        self.start = 0
        self.remaining = 0
        self.total = 0
        self.suitDeptIndex = None
        self.suitTypeIndex = None
        self.flags = 0
        self.air.netMessenger.accept('startInvasion', self, self.handleStartInvasion)
        self.air.netMessenger.accept('stopInvasion', self, self.handleStopInvasion)
        self.air.netMessenger.accept('queryShardStatus', self, self.sendInvasionStatus)
        self.sendInvasionStatus()

    def getInvading(self):
        return self.invading

    def getInvadingCog(self):
        return (self.suitDeptIndex, self.suitTypeIndex, self.flags)

    def startInvasion(self, suitDeptIndex = None, suitTypeIndex = None, flags = 0, type = INVASION_TYPE_NORMAL):
        if self.invading:
            return False
        if suitDeptIndex is None and suitTypeIndex is None and not flags:
            return False
        if flags and (suitDeptIndex is not None or suitTypeIndex is not None):
            return False
        if suitDeptIndex is None and suitTypeIndex is not None:
            return False
        if flags not in (0,
         IFV2,
         IFSkelecog,
         IFWaiter):
            return False
        if suitDeptIndex is not None and suitDeptIndex >= len(SuitDNA.suitDepts):
            return False
        if suitTypeIndex is not None and suitTypeIndex >= SuitDNA.suitsPerDept:
            return False
        if type not in (INVASION_TYPE_NORMAL, INVASION_TYPE_MEGA):
            return False
        self.invading = True
        self.start = int(time.time())
        self.suitDeptIndex = suitDeptIndex
        self.suitTypeIndex = suitTypeIndex
        self.flags = flags
        if type == INVASION_TYPE_NORMAL:
            self.total = 1000
        elif type == INVASION_TYPE_MEGA:
            self.total = 4294967295L
        self.remaining = self.total
        self.flySuits()
        self.notifyInvasionStarted()
        if self.suitDeptIndex is not None:
            self.air.districtStats.b_setInvasionStatus(self.suitDeptIndex + 1)
        else:
            self.air.districtStats.b_setInvasionStatus(5)
        if type == INVASION_TYPE_NORMAL:
            timeout = config.GetInt('invasion-timeout', 1800)
            taskMgr.doMethodLater(timeout, self.stopInvasion, 'invasionTimeout')
        self.sendInvasionStatus()
        return True

    def stopInvasion(self, task = None):
        if not self.invading:
            return False
        taskMgr.remove('invasionTimeout')
        self.air.districtStats.b_setInvasionStatus(0)
        self.notifyInvasionEnded()
        self.invading = False
        self.start = 0
        self.suitDeptIndex = None
        self.suitTypeIndex = None
        self.flags = 0
        self.total = 0
        self.remaining = 0
        self.flySuits()
        self.sendInvasionStatus()
        return True

    def getSuitName(self):
        if self.suitDeptIndex is not None:
            if self.suitTypeIndex is not None:
                return SuitDNA.getSuitName(self.suitDeptIndex, self.suitTypeIndex)
            else:
                return SuitDNA.suitDepts[self.suitDeptIndex]
        else:
            return SuitDNA.suitHeadTypes[0]

    def notifyInvasionStarted(self):
        msgType = ToontownGlobals.SuitInvasionBegin
        if self.flags & IFSkelecog:
            msgType = ToontownGlobals.SkelecogInvasionBegin
        elif self.flags & IFWaiter:
            msgType = ToontownGlobals.WaiterInvasionBegin
        elif self.flags & IFV2:
            msgType = ToontownGlobals.V2InvasionBegin
        self.air.newsManager.sendUpdate('setInvasionStatus', [msgType,
         self.getSuitName(),
         self.total,
         self.flags])

    def notifyInvasionEnded(self):
        msgType = ToontownGlobals.SuitInvasionEnd
        if self.flags & IFSkelecog:
            msgType = ToontownGlobals.SkelecogInvasionEnd
        elif self.flags & IFWaiter:
            msgType = ToontownGlobals.WaiterInvasionEnd
        elif self.flags & IFV2:
            msgType = ToontownGlobals.V2InvasionEnd
        self.air.newsManager.sendUpdate('setInvasionStatus', [msgType,
         self.getSuitName(),
         0,
         self.flags])

    def notifyInvasionUpdate(self):
        self.air.newsManager.sendUpdate('setInvasionStatus', [ToontownGlobals.SuitInvasionUpdate,
         self.getSuitName(),
         self.remaining,
         self.flags])

    def notifyInvasionBulletin(self, avId):
        msgType = ToontownGlobals.SuitInvasionBulletin
        if self.flags & IFSkelecog:
            msgType = ToontownGlobals.SkelecogInvasionBulletin
        elif self.flags & IFWaiter:
            msgType = ToontownGlobals.WaiterInvasionBulletin
        elif self.flags & IFV2:
            msgType = ToontownGlobals.V2InvasionBulletin
        self.air.newsManager.sendUpdateToAvatarId(avId, 'setInvasionStatus', [msgType,
         self.getSuitName(),
         self.remaining,
         self.flags])

    def flySuits(self):
        for suitPlanner in self.air.suitPlanners.values():
            suitPlanner.flySuits()

    def handleSuitDefeated(self):
        self.remaining -= 1
        if self.remaining == 0:
            self.stopInvasion()
        elif self.remaining == self.total / 2:
            self.notifyInvasionUpdate()
        self.sendInvasionStatus()

    def handleStartInvasion(self, shardId, *args):
        if shardId == self.air.ourChannel:
            self.startInvasion(*args)

    def handleStopInvasion(self, shardId):
        if shardId == self.air.ourChannel:
            self.stopInvasion()

    def sendInvasionStatus(self):
        if self.invading:
            if self.suitDeptIndex is not None:
                if self.suitTypeIndex is not None:
                    type = SuitBattleGlobals.SuitAttributes[self.getSuitName()]['name']
                else:
                    type = SuitDNA.getDeptFullname(self.getSuitName())
            else:
                type = None
            status = {'invasion': {'type': type,
                          'flags': self.flags,
                          'remaining': self.remaining,
                          'total': self.total,
                          'start': self.start}}
        else:
            status = {'invasion': None}
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, status])
