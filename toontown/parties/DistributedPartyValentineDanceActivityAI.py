#Embedded file name: toontown.parties.DistributedPartyValentineDanceActivityAI
from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyDanceActivityBaseAI import DistributedPartyDanceActivityBaseAI

class DistributedPartyValentineDanceActivityAI(DistributedPartyDanceActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyValentineDanceActivityAI')
