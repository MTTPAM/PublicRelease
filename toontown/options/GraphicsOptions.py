#Embedded file name: toontown.options.GraphicsOptions
from panda3d.core import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
resolution_table = [(800, 600),
 (1024, 768),
 (1280, 1024),
 (1600, 1200),
 (1280, 720),
 (1920, 1080)]
AspectRatios = [0,
 1.33333,
 1.25,
 1.77777,
 2.33333]
AspectRatioLabels = ['Adaptive',
 '4:3',
 '5:3',
 '16:9',
 '21:9']

class GraphicsOptions:

    def setTextureScale(self):
        pass
