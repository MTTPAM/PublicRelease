#Embedded file name: toontown.safezone.DistributedGameTableAI
from direct.distributed import DistributedObjectAI

class DistributedGameTableAI(DistributedObjectAI.DistributedObjectAI):

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.posHpr = (0, 0, 0, 0, 0, 0)

    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = (x,
         y,
         z,
         h,
         p,
         r)

    def getPosHpr(self):
        return self.posHpr

    def requestJoin(self, seatIndex):
        avId = self.air.getAvatarIdFromSender()
        self.sendUpdateToAvatarId(avId, 'rejectJoin', [])

    def requestExit(self):
        pass
