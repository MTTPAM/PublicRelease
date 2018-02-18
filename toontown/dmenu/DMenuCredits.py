#Embedded file name: toontown.dmenu.DMenuCredits
from panda3d.core import Vec4, TransparencyAttrib, Point3, VBase3, VBase4, TextNode
from direct.interval.IntervalGlobal import *
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals

class DMenuCredits:

    def __init__(self):
        self.creditsSequence = None
        self.text = None
        self.roleText = None
        cm = CardMaker('screen-cover')
        cm.setFrameFullscreenQuad()
        self.screenCover = aspect2d.attachNewNode(cm.generate())
        self.screenCover.show()
        self.screenCover.setScale(100)
        self.screenCover.setColor((0, 0, 0, 1))
        self.screenCover.setTransparency(1)
        self.extremelylargecredits = '\n\x01orangeText\x01Credits\x02\n\n\x01orangeText\x01Management Team\x02\nDubito | Director\nBethy / Limey Mouse | Director\nRoyko | External Community Manager\nLoopy Goopy Googlenerd | Content Director\n\n\x01orangeText\x01Technical Team\x02\nSir Tubby Cheezyfish | Lead Game Developer\nBarks | Game Developer\nTessler | Game Developer \nAtomizer | Game Developer \nNosyliam | Game Developer \nBen | Launcher Developer\nJudge2020 | Launcher Developer\nXanon | Web Developer\n\n\x01orangeText\x01Creative Team\x02\nBethy / Limey Mouse | Lead Artist\nOld Geezer | Modeller | Composer\nPolygon | Modeller\nMaddie | Texture Artist\nVoidPoro | Texture Artist\nPascal | Modeller | Head of Moderation\nSpookiRandi | Graphical Artist\n\n\x01orangeText\x01Moderation Team\x02\nDr. Sovietoon\nTheTabKey\nKryptic Kaleidoscope\nThe Professional\nSpookiRandi\n\n\x01orangeText\x01Contributors\x02\nDank Mickey | Former Developer | Boardbot Development\nJosh Zimmer | Former Developer\nSkippsDev | Former Developer\nSwag Foreman | Boardbot Models | Various parts of Cog Rooftops\nAura | Pick-A-Toon Concept / Inspiration\nSmirky Bumberpop | Former External Community Manager\nMalverde | Former Developer | Various playground redesigns\nAlice | Web Developer\n\n\x01orangeText\x01Special thanks to\x02\nToontown Infinite | Various Resources\nPiplup | New battle GUI concept\nChandler | DNA Parser | Safely disclosing security issues\nDevelopers of Panda3D\nDevelopers of Astron\nToontown Rewritten | Reviving the spirit of Toontown\n'
        self.text = OnscreenText(text=self.extremelylargecredits, style=3, fg=(1, 1, 1, 1), align=TextNode.ACenter, scale=0.08, wordwrap=30, parent=aspect2d)
        self.text.setPos(0, -1)
        self.text.setColorScale(1, 1, 1, 0)
        self.logo = OnscreenImage(image='phase_3/maps/toontown-logo.png', scale=(0.8 * (4.0 / 3.0), 0.8, 0.8 / (4.0 / 3.0)))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.logo.reparentTo(self.text)
        self.logo.setPos(0, 0, 0)
        self.logo.setColorScale(1, 1, 1, 1)
        self.startCredits()
        base.transitions.fadeScreen(0)
        base.accept('space', self.removeCredits)
        base.accept('escape', self.removeCredits)

    def startCredits(self):
        self.creditsSequence = Sequence(LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0)), LerpColorScaleInterval(self.text, 1, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0)), Wait(1), self.text.posInterval(35, Point3(0, 0, 6)), Wait(1), LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1)), Func(self.removeCredits)).start()

    def removeCredits(self):
        base.ignore('space')
        base.ignore('escape')
        base.transitions.noFade()
        if self.creditsSequence:
            self.creditsSequence.finish()
            self.creditsSequence = None
        if self.text:
            self.text.destroy()
            self.text = None
        if self.screenCover:
            self.screenCover.removeNode()
            self.screenCover = None
