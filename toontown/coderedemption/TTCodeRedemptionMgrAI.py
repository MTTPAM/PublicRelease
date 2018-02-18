#Embedded file name: toontown.coderedemption.TTCodeRedemptionMgrAI
import time
from datetime import datetime
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.catalog import CatalogItem
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem
from toontown.catalog.CatalogClothingItem import CatalogClothingItem
from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.catalog.CatalogPoleItem import CatalogPoleItem
from toontown.catalog.CatalogBeanItem import CatalogBeanItem
from toontown.catalog.CatalogChatItem import CatalogChatItem
from toontown.catalog.CatalogAccessoryItem import CatalogAccessoryItem
from toontown.catalog.CatalogRentalItem import CatalogRentalItem
from toontown.catalog.CatalogGardenItem import CatalogGardenItem
from toontown.catalog.CatalogGardenStarterItem import CatalogGardenStarterItem
from toontown.coderedemption import TTCodeRedemptionConsts, TTCodeRedemptionGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toon import ToonDNA
from toontown.toon import NPCToons

class TTCodeRedemptionMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTCodeRedemptionMgrAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def delete(self):
        DistributedObjectAI.delete(self)

    def giveAwardToToonResult(self, todo0, todo1):
        pass

    def redeemCode(self, context, code):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to redeem a code from an invalid avId')
            return
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Invalid avatar tried to redeem a code')
            return
        isValid = True
        hasExpired = False
        isEligible = True
        beenDelivered = False
        code = str(code.lower().replace(' ', '').replace('-', '').replace('_', ''))
        avCodes = av.getRedeemedCodes()
        if not avCodes:
            avCodes = [code]
            av.b_setRedeemedCodes(avCodes)
        elif code not in avCodes:
            avCodes.append(code)
            av.b_setRedeemedCodes(avCodes)
            isEligible = True
        else:
            isEligible = False
        expirationDate = TTCodeRedemptionGlobals.codeToExpiration.get(code)
        if not expirationDate:
            hasExpired = False
        elif datetime.now() > expirationDate:
            hasExpired = True
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to redeem a code from an invalid avId')
            return
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Invalid avatar tried to redeem a code')
            return
        if not isValid:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Invalid code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, ToontownGlobals.CODE_INVALID, 0])
            return
        if hasExpired:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Expired code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, ToontownGlobals.CODE_EXPIRED, 0])
            return
        if not isEligible:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Ineligible for code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, ToontownGlobals.CODE_INELIGIBLE, 0])
            return
        items = self.getItemsForCode(code)
        for item in items:
            if isinstance(item, CatalogInvalidItem):
                self.air.writeServerEvent('suspicious', avId=avId, issue='uh oh! invalid item type for code: %s' % code)
                self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, ToontownGlobals.CODE_INVALID, 0])
                break
            if len(av.mailboxContents) + len(av.onGiftOrder) >= ToontownGlobals.MaxMailboxContents:
                beenDelivered = False
                break
            item.deliveryDate = int(time.time() / 60) + 1
            av.onOrder.append(item)
            av.b_setDeliverySchedule(av.onOrder)
            beenDelivered = True

        if not beenDelivered:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Could not deliver items for code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, ToontownGlobals.CODE_INVALID, 0])
            return
        self.air.writeServerEvent('code-redeemed', avId=avId, issue='Successfuly redeemed code: %s' % code)
        self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, ToontownGlobals.CODE_SUCCESS, 0])

    def getItemsForCode(self, code):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='AVID is none')
            return
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Avatar doesnt exist')
            return
        code = str(code.lower().replace(' ', '').replace('-', '').replace('_', ''))
        allinsomniacodes = []
        codefile = open('data/insomnia_codes.txt', 'r')
        insomniacodes = codefile.read().split('\n')
        for line in insomniacodes:
            allinsomniacodes.append(line)

        codefile.close()
        if code in allinsomniacodes and code != '':
            with open('data/insomnia_codes.txt', 'w') as file:
                allinsomniacodes.remove(code)
                for code in allinsomniacodes:
                    file.write(code + '\n')

                file.close()
            shirt = CatalogClothingItem(4120, 0)
            dna = ToonDNA.ToonDNA()
            dna.makeFromNetString(av.getDNAString())
            if dna.gender == 'm':
                shorts = CatalogClothingItem(4121, 0)
            else:
                shorts = CatalogClothingItem(4122, 0)
            return [shirt, shorts]
        if code == 'sillymeter':
            shirt = CatalogClothingItem(1753, 0)
            return [shirt]
        if code == 'getconnected':
            shirt = CatalogClothingItem(1752, 0)
            return [shirt]
        if code == 'toontastic':
            shirt = CatalogClothingItem(1820, 0)
            return [shirt]
        return []

    def redeemCodeAiToUd(self, avId, context, code):
        self.sendUpdate('redeemCodeAiToUd', [avId, context, code])

    def redeemCodeResultUdToAi(self, avId, context, result, awardMgrResult):
        self.d_redeemCodeResult(avId, context, result, awardMgrResult)

    def d_redeemCodeResult(self, avId, context, result, awardMgrResult):
        self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, result, awardMgrResult])
