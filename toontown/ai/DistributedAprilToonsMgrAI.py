#Embedded file name: toontown.ai.DistributedAprilToonsMgrAI
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.ai.MagicWordGlobal import *
from direct.task import Task
from toontown.toonbase.AprilToonsGlobals import *

class DistributedAprilToonsMgrAI(DistributedObjectAI):

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.events = [EventRandomDialogue,
         EventRandomEffects,
         EventEstateGravity,
         EventGlobalGravity]

    def getEvents(self):
        return self.events

    def isEventActive(self, eventId):
        if not self.air.config.GetBool('want-april-toons', False):
            return False
        return eventId in self.events

    def requestEventsList(self):
        avId = self.air.getAvatarIdFromSender()
        self.sendUpdateToAvatarId(avId, 'requestEventsListResp', [self.getEvents()])

    def toggleEvent(self, eventId):
        if eventId in self.getEvents():
            del self.getEvents()[eventId]
            self.sendUpdate('setEventActive', [eventId, False])
        else:
            self.getEvents().append(eventId)
            self.sendUpdate('setEventActive', [eventId, True])
