from character import Character
import random
import time

class Thief(Character):
    def __init__(self, name):
        super().__init__(name, 6, 1, 15, 3, 0, 6)
    
    def attack(self, enemy):
        if not self.is_alive(enemy):
            return
        print("%s attacks %s" % (self.name, enemy.name))
        self.steal_coins(enemy)
        critical_chance = random.randint(1, 5)
        if critical_chance > 4:
            enemy.receive_damage(self.power * 2)
            print("Critical hit!")
        else: 
            enemy.receive_damage(self.power)
        time.sleep(0.5)

    def steal_coins(self, enemy):
        enemy.coins -= self.power
        self.bounty += self.power
        print(f"{self.name} stole {self.power} coins!")