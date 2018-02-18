from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import AppRunnerGlobal
import os

class BattleSounds:
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleSounds')

    def __init__(self):
        self.mgr = AudioManager.createAudioManager()
        self.isValid = 0
        if self.mgr != None and self.mgr.isValid():
            self.isValid = 1
            limit = base.config.GetInt('battle-sound-cache-size', 15)
            self.mgr.setCacheLimit(limit)
            base.addSfxManager(self.mgr)
            self.setupSearchPath()

    def setupSearchPath(self):
        self.sfxSearchPath = DSearchPath()
        for phase in (3, 3.5, 4, 5):
            self.sfxSearchPath.appendDirectory(Filename('resources/phase_%s/audio/sfx' % phase))

    def clear(self):
        if self.isValid:
            self.mgr.clearCache()

    def getSound(self, name):
        if self.isValid:
            filename = Filename(name)
            found = vfs.resolveFilename(filename, self.sfxSearchPath)
            if not found:
                self.setupSearchPath()
                found = vfs.resolveFilename(filename, self.sfxSearchPath)
            if not found:
                self.notify.warning('%s not found on:' % name)
                print self.sfxSearchPath
            else:
                return self.mgr.getSound(filename.getFullpath())
        return self.mgr.getNullSound()

globalBattleSoundCache = BattleSounds()
