class Evade:
    cost = 8
    name = 'evade'
    can_be_used = False
    def apply(self, hero, enemy):
        hero.evade += 2
        hero.change_evade(hero.evade)
        print(f"{hero.name}'s evade chance increased to {round(hero.evade_percentage * 100, 1)}.'")