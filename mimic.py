from character import Character
import random
import time
# I want him to inherit random traits from other characters for one round
# To do this, set a trait that is the random trait selected to be used
# Set if statements inside traits to run only when selected, otherwise, super
# 
class Mimic(Character):
    def __init__(self, name):
        super().__init__(name, 15, 0, 1, 1, 0, 15)
        self.random_trait = random.randint(1, 6)
    
    def attack(self, enemy):
        if not self.is_alive(enemy):
            return
        if self.random_trait == 1:
            print("%s attacks %s" % (self.name, enemy.name))
            enemy.receive_damage(self.power * 2)
            print("Critical hit!")
            time.sleep(0.5)
        elif self.random_trait == 3:
            self.power = self.power * 2
            print("%s goes Super-Sayan and doubles his power to %s" % (self.name, self.power))
        elif self.random_trait == 4:
            self.steal_coins(enemy)
        elif self.random_trait == 6:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
            super().attack(enemy)
            self.power, enemy.power = enemy.power, self.power
            return
        super().attack(enemy)
    
    def receive_damage(self, points):
        if self.random_trait == 5:
            self.evade = 23
            print(f"{self.name} darts about nimbly.")
            super().receive_damage(points)
            print(f"{self.name} stops dancing.")
            self.evade = 1
        else:
            super().receive_damage(points)
            if self.random_trait == 2:
                self.health += 2
                print(f"{self.name} healed 2 points!")
        self.change_trait()
    
    def steal_coins(self, enemy):
        if enemy.coins > self.power:
            enemy.coins -= self.power
            self.bounty += self.power
            print(f"{self.name} stole {self.power} coins!")
        elif enemy.coins == 0:
            print(f"{enemy.name} has no coins to steal.")
        else:
            enemy.coins = 0
            print(f"{self.name} stole {enemy.name}'s last coins.")

    def change_trait(self):
        self.random_trait = random.randint(1, 6)
    
    
    
    