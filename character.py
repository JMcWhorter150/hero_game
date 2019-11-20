import math
import random
import time

class Character(object):
    def __init__(self, name='<undefined>', health=10, armor=0, evade=1, power=5, coins=20, bounty=5,  items=[], holy_status=False):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.coins = coins
        self.bounty = bounty
        self.evade = evade
        self.evade_percentage = self.determine_evade(evade)
        self.holy_status = holy_status
        self.items = items
    
    def determine_evade(self, evade):
        evade_percentage = 1 - math.exp(-1*(evade/10))
        return evade_percentage
    
    def change_evade(self, evade):
        self.evade_percentage = self.determine_evade(self.evade)

    def is_alive(self, *args):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive(enemy):
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(0.5)

    def receive_damage(self, points):
        avoid_damage_chance = random.random()
        if avoid_damage_chance < self.evade_percentage:
            print(f"{self.name} dodged the attack and receives no damage!")
        else:
            points -= self.armor
            if points <= 0:
                print(f"Armor absorbed the damage. {self.name} took no damage.")
            else:
                self.health -= points
                print("%s received %d damage. Armor reduced %d damage." % (self.name, points, self.armor))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power and %d armor." % (self.name, self.health, self.power, self.armor))

    def give_bounty(self, enemy):
        enemy.coins += self.bounty
        print(f"{enemy.name} receives {self.bounty} coins from {self.name}'s coin purse.")