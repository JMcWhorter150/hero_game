from character import Character
import random

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 10, 2, 1, 1, 0, 6)
    
    def receive_damage(self, points):
        super().receive_damage(points)

        if random.random() < 0.2:
            self.health += 2
            print(f"{self.name} healed 2 points!")