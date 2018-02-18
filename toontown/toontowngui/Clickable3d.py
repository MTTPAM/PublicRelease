#Embedded file name: toontown.toontowngui.Clickable3d
from panda3d.core import Quat, Point3, Point2
from toontown.toontowngui.Clickable import Clickable

class Clickable3d(Clickable):

    def setClickRegionFrame(self, left, right, bottom, top):
        transform = self.contents.getNetTransform()
        camTransform = base.cam.getNetTransform().getInverse()
        transform = camTransform.compose(transform)
        transform.setQuat(Quat())
        mat = transform.getMat()
        camSpaceTopLeft = mat.xformPoint(Point3(left, 0, top))
        camSpaceBottomRight = mat.xformPoint(Point3(right, 0, bottom))
        screenSpaceTopLeft = Point2()
        screenSpaceBottomRight = Point2()
        base.camLens.project(Point3(camSpaceTopLeft), screenSpaceTopLeft)
        base.camLens.project(Point3(camSpaceBottomRight), screenSpaceBottomRight)
        left, top = screenSpaceTopLeft
        right, bottom = screenSpaceBottomRight
        self.region.setFrame(left, right, bottom, top)
