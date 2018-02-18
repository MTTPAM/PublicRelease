#Embedded file name: toontown.uberdog.ClientServicesManager
import hmac
import httplib
import urllib
import json
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from pandac.PandaModules import *
from otp.distributed.PotentialAvatar import PotentialAvatar
from otp.otpbase import OTPGlobals
from toontown.chat.ChatGlobals import WTSystem
from toontown.chat.WhisperPopup import WhisperPopup



class ClientServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ClientServicesManager')

    def __init__(self, air):
        DistributedObjectGlobal.__init__(self, air)

    # --- LOGIN LOGIC ---
    def performLogin(self, doneEvent):
        self.doneEvent = doneEvent

        self.systemMessageSfx = None

        token = self.cr.playToken or 'dev'

        key = 'bG9sLndlLmNoYW5nZS50aGlzLnRvby5tdWNo'
        digest_maker = hmac.new(key)
        digest_maker.update(token)
        clientKey = digest_maker.hexdigest()

        self.sendUpdate('login', [token, clientKey])

    def acceptLogin(self, timestamp):
        messenger.send(self.doneEvent, [{'mode': 'success', 'timestamp': timestamp}])


    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

    def setMOTD(self, motd):
        base.cr.motdText = motd

    def setAvatars(self, avatars):
        avList = []
        for avNum, avName, avDNA, avPosition, nameState, hp, maxHp in avatars:
            nameOpen = int(nameState == 1)
            names = [avName,
             '',
             '',
             '']
            if nameState == 2:
                names[1] = avName
            elif nameState == 3:
                names[2] = avName
            elif nameState == 4:
                names[3] = avName
            avList.append(PotentialAvatar(avNum, names, avDNA, avPosition, nameOpen, hp=hp, maxHp=maxHp))

        self.cr.handleAvatarsList(avList)

    def sendCreateAvatar(self, avDNA, _, index, uber, tracks, pg):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(),
         index,
         uber,
         tracks,
         pg])

    def createAvatarResp(self, avId):
        messenger.send('nameShopCreateAvatarDone', [avId])

    def sendDeleteAvatar(self, avId):
        self.sendUpdate('deleteAvatar', [avId])

    def sendSetNameTyped(self, avId, name, callback):
        self._callback = callback
        self.sendUpdate('setNameTyped', [avId, name])

    def setNameTypedResp(self, avId, status):
        self._callback(avId, status)

    def sendSetNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4, callback):
        self._callback = callback
        self.sendUpdate('setNamePattern', [avId,
         p1,
         f1,
         p2,
         f2,
         p3,
         f3,
         p4,
         f4])

    def setNamePatternResp(self, avId, status):
        self._callback(avId, status)

    def sendAcknowledgeAvatarName(self, avId, callback):
        self._callback = callback
        self.sendUpdate('acknowledgeAvatarName', [avId])

    def acknowledgeAvatarNameResp(self):
        self._callback()

    def sendChooseAvatar(self, avId):
        self.sendUpdate('chooseAvatar', [avId])

    def systemMessage(self, message):
        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WTSystem)
        whisper.manage(base.marginManager)
        if hasattr(base.cr, 'chatLog'):
            base.cr.chatLog.addToLog('\x01orangeText\x01System Message: %s\x02' % message)
        base.playSfx(base.loader.loadSfx('phase_3/audio/sfx/clock03.ogg'))
