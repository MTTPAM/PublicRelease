#Embedded file name: toontown.distributed.NonRepeatableRandomSourceAI
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.task import Task
from otp.distributed import OtpDoGlobals
import random

class NonRepeatableRandomSourceAI(DistributedObjectAI):
    notify = directNotify.newCategory('NonRepeatableRandomSourceAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self._contextGen = SerialMaskedGen(4294967295L)
        self._requests = {}
        self._sampleTask = self.doMethodLater(180, self._sampleRandomTask, self.uniqueName('sampleRandom'))
        self._sampleRandom()

    def delete(self):
        self.removeTask(self._sampleTask)
        self._sampleTask = None
        DistributedObjectAI.delete(self)

    def _sampleRandomTask(self, task = None):
        self._sampleRandom()
        return Task.again

    def _sampleRandom(self):
        self.air.sendUpdateToDoId('NonRepeatableRandomSource', 'randomSample', OtpDoGlobals.OTP_DO_ID_TOONTOWN_NON_REPEATABLE_RANDOM_SOURCE, [self.doId, int(random.randrange(4294967296L))])

    def randomSampleAck(self):
        self._sampleRandom()

    def getRandomSamples(self, callback, num = None):
        if num is None:
            num = 1
        context = self._contextGen.next()
        self._requests[context] = (callback,)
        self.air.sendUpdateToDoId('NonRepeatableRandomSource', 'getRandomSamples', OtpDoGlobals.OTP_DO_ID_TOONTOWN_NON_REPEATABLE_RANDOM_SOURCE, [self.doId,
         'NonRepeatableRandomSource',
         context,
         num])

    def getRandomSamplesReply(self, context, samples):
        callback, = self._requests.pop(context)
        callback(samples)
