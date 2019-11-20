class HolyWater:
    cost = 15
    name = 'holy water'
    can_be_used = True
    def apply(self, hero, enemy):
        hero.holy_status = True
        print(f"{hero.name} is no longer afraid of the undying.")