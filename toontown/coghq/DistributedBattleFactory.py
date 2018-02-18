#Embedded file name: toontown.coghq.DistributedBattleFactory
import random
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleBase import *
from toontown.coghq import DistributedLevelBattle
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import TTEmote
from otp.avatar import Emote
from toontown.battle import SuitBattleGlobals
from toontown.suit import SuitDNA
from direct.fsm import State
from direct.fsm import ClassicFSM, State
from toontown.toonbase import ToontownGlobals
from toontown.nametag import NametagGlobals

class DistributedBattleFactory(DistributedLevelBattle.DistributedLevelBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleFactory')

    def __init__(self, cr):
        DistributedLevelBattle.DistributedLevelBattle.__init__(self, cr)
        self.fsm.addState(State.State('FactoryReward', self.enterFactoryReward, self.exitFactoryReward, ['Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('FactoryReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('FactoryReward')

    def enterFactoryReward(self, ts):
        self.notify.info('enterFactoryReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setWant2dNametags(False)
            if self.bossBattle:
                messenger.send('localToonConfrontedForeman')
        self.movie.playReward(ts, self.uniqueName('building-reward'), self.__handleFactoryRewardDone, noSkip=True)

    def __handleFactoryRewardDone(self):
        self.notify.info('Factory reward done')
        if self.hasLocalToon():
            self.d_rewardDone(base.localAvatar.doId)
        self.movie.resetReward()
        self.fsm.request('Resume')

    def exitFactoryReward(self):
        self.notify.info('exitFactoryReward()')
        self.movie.resetReward(finish=1)
        self._removeMembersKeep()
        NametagGlobals.setWant2dNametags(True)
