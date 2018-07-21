from RuneManager import RuneManager

class AttackRune:
    def __init__(self, dmgBonus):
        self.dmgBonus = dmgBonus

    def provideEffect(self):
        RuneManager.doDmgBonus(self.dmgBonus)

class HealthRune:
    def __init__(self, hpBonus):
        self.hpBonus = hpBonus

    def provideEffect(self):
        RuneManager.doHpBonus(self.hpBonus)

runeDict = (
 AttackRune(dmgBonus=5),
 AttackRune(dmgBonus=8),
 AttackRune(dmgBonus=11),
 HealthRune(hpBonus=2),
 HealthRune(hpBonus=3),
 HealthRune(hpBonus=4)
 )

rune2Id = {
 AttackRune: [0, 1, 2],
 HealthRune: [3, 4, 5]
 }

runeNames = [
 'Tier 1 Damage',
 'Tier 2 Damage',
 'Tier 3 Damage',
 'Tier 1 Health',
 'Tier 2 Health',
 'Tier 3 Health'
 ]

runeDescriptions = [
 'Provides 5 extra gag damage.',
 'Provides 8 extra gag damage.',
 'Provides 11 extra gag damage.',
 'Provides 2 extra laff points.',
 'Provides 3 extra laff points.',
 'Provides 4 extra laff points.'
 ]