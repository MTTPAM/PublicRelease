#Embedded file name: toontown.shtiker.DisguisePage
from toontown.shtiker import ShtikerPage
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.direct import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.suit import SuitDNA
from toontown.battle import SuitBattleGlobals
from toontown.minigame import MinigamePowerMeter
from toontown.coghq import CogDisguiseGlobals
DeptColors = (Vec4(0.647, 0.608, 0.596, 1.0),
 Vec4(0.588, 0.635, 0.671, 1.0),
 Vec4(0.596, 0.714, 0.659, 1.0),
 Vec4(0.761, 0.678, 0.69, 1.0),
 Vec4(0.5, 0.5, 0.5, 1.0))
PartNames = ('lUpleg', 'lLowleg', 'lShoe', 'rUpleg', 'rLowleg', 'rShoe', 'lShoulder', 'rShoulder', 'chest', 'waist', 'hip', 'lUparm', 'lLowarm', 'lHand', 'rUparm', 'rLowarm', 'rHand')

class DisguisePage(ShtikerPage.ShtikerPage):
    meterColor = Vec4(0.87, 0.87, 0.827, 1.0)
    meterActiveColor = Vec4(0.7, 0.3, 0.3, 1)

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.activeTab = 0
        self.progressTitle = None

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        gui = loader.loadModel('phase_9/models/gui/cog_disguises')
        icons = loader.loadModel('phase_3/models/gui/cog_icons')
        self.frame = DirectFrame(parent=self, relief=None, scale=0.47, pos=(0.1, 1, 0))
        self.bkgd = DirectFrame(parent=self.frame, geom=gui.find('**/base'), relief=None, scale=(0.98, 1, 1))
        self.bkgd.setTextureOff(1)
        self.buttons = []
        self.pageFrame = DirectFrame(parent=self.frame, relief=None)
        self.xOffset = 0.4
        self.deptLabel = DirectLabel(parent=self.frame, text='', text_font=ToontownGlobals.getSuitFont(), text_style=3, text_fg=(1, 1, 1, 1), text_scale=TTLocalizer.DPdeptLabel, text_pos=(-0.1, 0.8))
        DirectFrame(parent=self.frame, relief=None, geom=gui.find('**/pipe_frame'))
        self.tube = DirectFrame(parent=self.frame, relief=None, geom=gui.find('**/tube'))
        DirectFrame(parent=self.frame, relief=None, geom=gui.find('**/robot/face'))
        DirectLabel(parent=self.frame, relief=None, geom=gui.find('**/text_cog_disguises'), geom_pos=(0, 0.1, 0))
        self.meritTitle = DirectLabel(parent=self.frame, relief=None, geom=gui.find('**/text_merit_progress'), geom_pos=(0, 0.1, 0))
        self.meritTitle.hide()
        self.cogbuckTitle = DirectLabel(parent=self.frame, relief=None, geom=gui.find('**/text_cashbuck_progress'), geom_pos=(0, 0.1, 0))
        self.cogbuckTitle.hide()
        self.juryNoticeTitle = DirectLabel(parent=self.frame, relief=None, geom=gui.find('**/text_jury_notice_progress'), geom_pos=(0, 0.1, 0))
        self.juryNoticeTitle.hide()
        self.stockOptionTitle = DirectLabel(parent=self.frame, relief=None, geom=gui.find('**/text_stock_option_progress'), geom_pos=(0, 0.1, 0))
        self.stockOptionTitle.hide()
        self.progressTitle = self.meritTitle
        self.promotionTitle = DirectLabel(parent=self.frame, relief=None, geom=gui.find('**/text_ready4promotion'), geom_pos=(0, 0.1, 0))
        self.cogName = DirectLabel(parent=self.frame, relief=None, text='', text_font=ToontownGlobals.getSuitFont(), text_scale=TTLocalizer.DPcogName, text_align=TextNode.ACenter, pos=(-0.948, 0, -1.15))
        self.cogLevel = DirectLabel(parent=self.frame, relief=None, text='', text_font=ToontownGlobals.getSuitFont(), text_scale=0.09, text_align=TextNode.ACenter, pos=(-0.91, 0, -1.02))
        self.partFrame = DirectFrame(parent=self.frame, relief=None)
        self.parts = []
        for partNum in xrange(0, 17):
            self.parts.append(DirectFrame(parent=self.partFrame, relief=None, geom=gui.find('**/robot/' + PartNames[partNum])))

        self.holes = []
        for partNum in xrange(0, 17):
            self.holes.append(DirectFrame(parent=self.partFrame, relief=None, geom=gui.find('**/robot_hole/' + PartNames[partNum])))

        self.cogPartRatio = DirectLabel(parent=self.frame, relief=None, text='', text_font=ToontownGlobals.getSuitFont(), text_scale=0.08, text_align=TextNode.ACenter, pos=(-0.91, 0, -0.82))
        self.cogMeritRatio = DirectLabel(parent=self.frame, relief=None, text='', text_font=ToontownGlobals.getSuitFont(), text_scale=0.08, text_align=TextNode.ACenter, pos=(0.45, 0, -0.36))
        meterFace = gui.find('**/meter_face_whole')
        meterFaceHalf = gui.find('**/meter_face_half')
        self.meterFace = DirectLabel(parent=self.frame, relief=None, geom=meterFace, color=self.meterColor, pos=(0.455, 0.0, 0.04))
        self.meterFaceHalf1 = DirectLabel(parent=self.frame, relief=None, geom=meterFaceHalf, color=self.meterActiveColor, pos=(0.455, 0.0, 0.04))
        self.meterFaceHalf2 = DirectLabel(parent=self.frame, relief=None, geom=meterFaceHalf, color=self.meterColor, pos=(0.455, 0.0, 0.04))
        for dept in xrange(len(SuitDNA.suitDepts)):
            button = DirectButton(parent=self.frame, relief=None, pos=(-1 + self.xOffset * dept, 0, 1.05), image=icons.find(SuitDNA.suitDeptModelPaths[dept]), image_scale=0.25, image2_color=(1, 1, 1, 0.75), command=self.doTab, extraArgs=[dept])
            self.buttons.append(button)

        self.frame.hide()
        self.activeTab = 3
        self.updatePage()

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)

    def enter(self):
        self.frame.show()
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.frame.hide()
        ShtikerPage.ShtikerPage.exit(self)

    def updatePage(self):
        self.doTab(self.activeTab)

    def updatePartsDisplay(self, index, numParts, numPartsRequired):
        partBitmask = 1
        groupingBitmask = CogDisguiseGlobals.PartsPerSuitBitmasks[index]
        previousPart = 0
        for part in self.parts:
            groupingBit = groupingBitmask & partBitmask
            if numParts & partBitmask & groupingBit:
                part.show()
                self.holes[self.parts.index(part)].hide()
                if groupingBit:
                    previousPart = 1
            elif not groupingBit and previousPart:
                part.show()
                self.holes[self.parts.index(part)].hide()
            else:
                self.holes[self.parts.index(part)].show()
                part.hide()
                previousPart = 0
            partBitmask = partBitmask << 1

    def updateMeritBar(self, dept):
        merits = base.localAvatar.cogMerits[dept]
        totalMerits = CogDisguiseGlobals.getTotalMerits(base.localAvatar, dept)
        if totalMerits == 0:
            progress = 1
        else:
            progress = min(merits / float(totalMerits), 1)
        self.updateMeritDial(progress)
        if base.localAvatar.readyForPromotion(dept):
            self.cogMeritRatio['text'] = TTLocalizer.DisguisePageMeritFull
            self.promotionTitle.show()
            self.progressTitle.hide()
        else:
            self.cogMeritRatio['text'] = '%d/%d' % (merits, totalMerits)
            self.promotionTitle.hide()
            self.progressTitle.show()

    def updateMeritDial(self, progress):
        if progress == 0:
            self.meterFaceHalf1.hide()
            self.meterFaceHalf2.hide()
            self.meterFace.setColor(self.meterColor)
        elif progress == 1:
            self.meterFaceHalf1.hide()
            self.meterFaceHalf2.hide()
            self.meterFace.setColor(self.meterActiveColor)
        else:
            self.meterFaceHalf1.show()
            self.meterFaceHalf2.show()
            self.meterFace.setColor(self.meterColor)
            if progress < 0.5:
                self.meterFaceHalf2.setColor(self.meterColor)
            else:
                self.meterFaceHalf2.setColor(self.meterActiveColor)
                progress = progress - 0.5
            self.meterFaceHalf2.setR(180 * (progress / 0.5))

    def doTab(self, index):
        self.activeTab = index
        self.bkgd.setColor(DeptColors[index])
        self.deptLabel['text'] = (SuitDNA.suitDeptFullnames[SuitDNA.suitDepts[index]],)
        cogIndex = base.localAvatar.cogTypes[index] + SuitDNA.suitsPerDept * index
        cog = SuitDNA.suitHeadTypes[cogIndex]
        self.progressTitle.hide()
        if SuitDNA.suitDepts[index] == 'm':
            self.progressTitle = self.cogbuckTitle
        elif SuitDNA.suitDepts[index] == 'l':
            self.progressTitle = self.juryNoticeTitle
        elif SuitDNA.suitDepts[index] == 'c':
            self.progressTitle = self.stockOptionTitle
        else:
            self.progressTitle = self.meritTitle
        self.progressTitle.show()
        self.cogName['text'] = SuitBattleGlobals.SuitAttributes[cog]['name']
        cogLevel = base.localAvatar.cogLevels[index]
        if base.localAvatar.cogReviveLevels[self.activeTab] > -1:
            cogLevel = base.localAvatar.cogReviveLevels[self.activeTab]
            self.cogLevel['text_scale'] = 0.065
            self.cogLevel['text'] = TTLocalizer.DisguisePageCogLevel % str(cogLevel + 1) + TTLocalizer.SkeleRevivePostFix
        else:
            self.cogLevel['text_scale'] = 0.09
            self.cogLevel['text'] = TTLocalizer.DisguisePageCogLevel % str(cogLevel + 1)
        numParts = base.localAvatar.cogParts[index]
        numPartsRequired = CogDisguiseGlobals.PartsPerSuit[index]
        self.updatePartsDisplay(index, numParts, numPartsRequired)
        self.updateMeritBar(index)
        self.cogPartRatio['text'] = '%d/%d' % (CogDisguiseGlobals.getTotalParts(numParts), numPartsRequired)
