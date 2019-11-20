class Sword:
    cost = 10
    name = 'sword'
    can_be_used = False
    def apply(self, hero, enemy):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))