#Embedded file name: toontown.environment.DistributedDayTimeManagerAI
from panda3d.core import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task.Task import Task
from toontown.toonbase import TTLocalizer
import random
import time
from direct.showbase import PythonUtil
import DayTimeGlobals
from DistributedWeatherMGRAI import DistributedWeatherMGRAI

class DistributedDayTimeManagerAI(DistributedWeatherMGRAI):
    notify = directNotify.newCategory('DistributedDayTimeManagerAI')

    def __init__(self, air):
        DistributedWeatherMGRAI.__init__(self, air)
        self.air = air
        self.interval = 150
        self.currentHour = air.startTime

    def announceGenerate(self):
        DistributedWeatherMGRAI.announceGenerate(self)
        self.d_update(self.currentHour)
        self.air.setHour(self.currentHour)
        taskMgr.doMethodLater(self.interval, self.update, 'time-update-%s' % id(self))

    def d_requestUpdate(self):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'update', [self.currentHour])

    def update(self, task):
        if self.currentHour >= 23:
            self.currentHour = 0
        self.currentHour += 1
        self.air.setHour(self.currentHour)
        self.d_update(self.currentHour)
        return task.again

    def d_update(self, currentHour):
        self.sendUpdate('update', [currentHour])

    def stop(self):
        self.currentHour = 0
        taskMgr.remove('time-update-%s' % id(self))
