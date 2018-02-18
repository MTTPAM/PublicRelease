
class RuneManager:
    def __init__(self):
        pass

    def doDmgBonus(self, dmgBonus):
        self.sendUpdate('doDmgBonus', [dmgBonus])

    def doHpBonus(self, hpBonus):
        self.sendUpdate('doHpBonus', [hpBonus])
