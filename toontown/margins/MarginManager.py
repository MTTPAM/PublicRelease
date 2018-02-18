#Embedded file name: toontown.margins.MarginManager
import random
from pandac.PandaModules import PandaNode
from toontown.margins.MarginCell import MarginCell

class MarginManager(PandaNode):

    def __init__(self):
        PandaNode.__init__(self, 'margins')
        self.cells = set()
        self.visibles = set()

    def addCell(self, x, y, a2dMarker, id):
        cell = MarginCell(id)
        cell.reparentTo(a2dMarker)
        cell.setPos(x, 0, y)
        cell.setScale(0.2)
        cell.setActive(True)
        self.cells.add(cell)
        self.reorganize()
        return cell

    def removeCell(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.reorganize()

    def addVisible(self, visible):
        self.visibles.add(visible)
        self.reorganize()

    def removeVisible(self, visible):
        if visible in self.visibles:
            self.visibles.remove(visible)
            self.reorganize()

    def getActiveCells(self):
        return [ cell for cell in self.cells if cell.getActive() ]

    def reorganize(self):
        activeCells = self.getActiveCells()
        visibles = list(self.visibles)
        visibles.sort(key=lambda visible: visible.getPriority(), reverse=True)
        visibles = visibles[:len(activeCells)]
        emptyCells = []
        for cell in activeCells:
            content = cell.getContent()
            if content in visibles:
                visibles.remove(content)
                continue
            elif content is not None:
                cell.setContent(None)
            emptyCells.append(cell)

        for visible in visibles:
            cell = visible.getLastCell()
            if cell not in emptyCells:
                cell = random.choice(emptyCells)
            cell.setContent(visible)
            emptyCells.remove(cell)
