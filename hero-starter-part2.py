"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
import math

class Character(object):
    def __init__(self, name='<undefined>', health=10, armor=0, evade=1, power=5, coins=20, bounty=5, holy_status=False):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.coins = coins
        self.bounty = bounty
        self.evade = evade
        self.evade_percentage = self.determine_evade(evade)
        self.holy_status = holy_status
    
    def determine_evade(self, evade):
        evade_percentage = 1 - math.exp(-1*(evade/10))
        return evade_percentage
    
    def change_evade(self, evade):
        self.evade_percentage = self.determine_evade(self.evade)

    def is_alive(self, enemy):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive(enemy):
            return
        print("%s attacks %s" % (self.name, enemy.name))
        critical_chance = random.randint(1, 5)
        if critical_chance > 4:
            enemy.receive_damage(self.power * 2)
            print("Critical hit!")
        else: 
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
        if not self.is_alive(enemy):
            print("Oh no! %s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power and %d armor." % (self.name, self.health, self.power, self.armor))

    def give_bounty(self, enemy):
        enemy.coins += self.bounty
        print(f"{enemy.name} receives {self.bounty} coins from {self.name}'s coin purse.")
    

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)    

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, 6, 0, 1, 2, 0, 5)

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

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 10, 2, 1, 1, 0, 6)
    
    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        heal_chance = random.randint(1, 5)
        if heal_chance > 4:
            print(f"{self.name} healed 2 points!")
            self.health += 2
        if not self.is_alive(enemy):
            print("Oh no! %s is dead." % self.name)

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name, 1, 0, 20, 2, 0, 10)
    
class Zombie(Character):
    def __init__(self, name):
        super().__init__(name, 1, 0, 1, 1, 0, 20)
    
    def is_alive(self, enemy):
        if enemy.holy_status:
            print(f"{enemy.name}'s holy light immolates {self.name}")
            return False
        if self.health <= 0:
            print(f"{self.name} is a zombie and can't die!")
        return True
    
    def is_enemy_holy(self, enemy):
        return enemy.holy_status

class Sayan(Character):
    def __init__(self, name):
        super().__init__(name, 8, 2, 4, 2, 0, 10)
    
    def attack(self, enemy):
        power_up_chance = random.random() > 0.5
        if power_up_chance:
            self.power = self.power * 2
            print("%s goes Super-Sayan and doubles his power to %s" % (self.name, self.power))
        super().attack(enemy)

# class Mimic(Character):
#     def __init__(self, name):
#         super().__init__(name, 10, 1, 0)
    
#     def change_shape(self):
        # remains current health but changes to a different character with different moves

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
        



class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("%s faces %s" % (hero.name, enemy.name))
        print("=====================")
        while hero.is_alive(enemy) and enemy.is_alive(hero):
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.is_alive(enemy):
            print("You defeated %s" % enemy.name)
            enemy.give_bounty(hero)
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class SuperTonic:
    cost = 20
    name = 'SuperTonic'
    def apply(self, character):
        if character.health < 10:
            character.health = 10
        else:
            character.health += 5
        print("%s's health increased to %d." % (character.name, character.health))
        
class Armor:
    cost = 15
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print(f"{hero.name}'s armor has increased to {hero.armor}")

class Sword:
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Evade:
    cost = 10
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        hero.change_evade(hero.evade)
        print(f"{hero.name}'s evade chance increased to {round(hero.evade_percentage * 100, 1)}.'")

class HolyWater:
    cost = 15
    name = 'holy water'
    def apply(self, hero):
        hero.holy_status = True
        print(f"{hero.name} is no longer afraid of the undying.")

class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade, HolyWater]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero('Oakley')
enemies = [Goblin('Bob'), Wizard('Jethro'), Medic('Mercy'), Thief('Barry'), Zombie('Rick'), Shadow('Matt'), Sayan('Goku')]
# enemies = [Thief('Barry')]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
