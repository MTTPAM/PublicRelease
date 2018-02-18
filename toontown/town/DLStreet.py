#Embedded file name: toontown.town.DLStreet
from toontown.town import Street

class DLStreet(Street.Street):

    def enter(self, requestStatus):
        Street.Street.enter(self, requestStatus)
        render.setColorScale(Vec4(0.55, 0.55, 0.65, 1))
        self.loader.hood.setDreamlandFog()

    def exit(self):
        Street.Street.exit(self)
        self.loader.hood.setNoFog()
        render.setColorScale(Vec4(1, 1, 1, 1))
