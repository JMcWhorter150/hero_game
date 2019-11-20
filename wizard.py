from character import Character
import random

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 8, 0, 1, 1, 0, 6)

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super().attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power