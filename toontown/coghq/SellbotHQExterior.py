#Embedded file name: toontown.coghq.SellbotHQExterior
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import CogHQExterior
from toontown.dna.DNAParser import loadDNAFileAI, DNAStorage
from toontown.hood import ZoneUtil

class SellbotHQExterior(CogHQExterior.CogHQExterior):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotHQExterior')

    def enter(self, requestStatus):
        CogHQExterior.CogHQExterior.enter(self, requestStatus)
        self.loader.hood.startSky()
        dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName(self.zoneId)
        loadDNAFileAI(dnaStore, dnaFileName)
        self.zoneVisDict = {}
        for i in xrange(dnaStore.getNumDNAVisGroupsAI()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            visGroup = dnaStore.getDNAVisGroupAI(i)
            visZoneId = int(base.cr.hoodMgr.extractGroupName(groupFullName))
            visZoneId = ZoneUtil.getTrueZoneId(visZoneId, self.zoneId)
            visibles = []
            for i in xrange(visGroup.getNumVisibles()):
                visibles.append(int(visGroup.visibles[i]))

            visibles.append(ZoneUtil.getBranchZone(visZoneId))
            self.zoneVisDict[visZoneId] = visibles

        base.cr.sendSetZoneMsg(self.zoneId, self.zoneVisDict.values()[0])

    def exit(self):
        self.loader.hood.stopSky()
        CogHQExterior.CogHQExterior.exit(self)
