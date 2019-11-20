from character import Character
import random

class Sayan(Character):
    def __init__(self, name):
        super().__init__(name, 8, 2, 4, 2, 0, 10)
    
    def attack(self, enemy):
        power_up_chance = random.random() > 0.5
        if power_up_chance:
            self.power = self.power * 2
            print("%s goes Super-Sayan and doubles his power to %s" % (self.name, self.power))
        super().attack(enemy)