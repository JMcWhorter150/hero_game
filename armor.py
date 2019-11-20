class Armor:
    cost = 15
    name = 'armor'
    can_be_used = False
    def apply(self, hero, enemy):
        hero.armor += 2
        print(f"{hero.name}'s armor has increased to {hero.armor}")