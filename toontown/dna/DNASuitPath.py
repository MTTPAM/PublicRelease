#Embedded file name: toontown.dna.DNASuitPath


class DNASuitPath(object):
    __slots__ = 'suitPoints'

    def __init__(self):
        self.suitPoints = []

    def __del__(self):
        del self.suitPoints

    def getNumPoints(self):
        return len(self.suitPoints)

    def getPointIndex(self, pointIndex):
        return self.suitPoints[pointIndex].getIndex()

    def addPoint(self, point):
        self.suitPoints.append(point)

    def getPoint(self, pointIndex):
        return self.suitPoints[pointIndex]

    def reversePath(self):
        self.suitPoints.reverse()
