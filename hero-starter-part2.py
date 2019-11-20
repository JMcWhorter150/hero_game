"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
import math

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

    def is_alive(self, enemy):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive(enemy):
            return
        print("%s attacks %s" % (self.name, enemy.name))
        critical_chance = random.randint(1, 5)
        if critical_chance > 4:
            enemy.receive_damage(self.power * 2)
            print(f"Critical hit! {self.name} did double damage to {enemy.name}")
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
        if self.coins < item.cost:
            print("Not enough coins.")
            return
        self.coins -= item.cost
        if item.can_be_used:    
            self.items.append(item)
        else:
            item.apply(hero, enemy)
    
    def use_item(self, items):
        print("You have the following items:")
        for i in range(len(self.items)):
            print(f"{i}. {self.items[i].name}")
        choosing_item = True
        while choosing_item:
            print("Which item do you want to use? ")
            user_input = int(input("> "))
            if user_input in range(len(self.items)):
                self.items[user_input].apply(hero, enemy)
                choosing_item = False
            else:
                print("Invalid user input")

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
            print("2. use an item")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                if hero.items == []:
                    print("You have no items.")
                    continue
                else:
                    hero.use_item(hero.items)
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
    can_be_used = True
    def apply(self, character, enemy):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class SuperTonic:
    cost = 20
    name = 'SuperTonic'
    can_be_used = True
    def apply(self, character, enemy):
        if character.health < 10:
            character.health = 10
        else:
            character.health += 5
        print("%s's health increased to %d." % (character.name, character.health))
        
class Armor:
    cost = 15
    name = 'armor'
    can_be_used = False
    def apply(self, hero, enemy):
        hero.armor += 2
        print(f"{hero.name}'s armor has increased to {hero.armor}")

class Sword:
    cost = 10
    name = 'sword'
    can_be_used = False
    def apply(self, hero, enemy):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Evade:
    cost = 10
    name = 'evade'
    can_be_used = False
    def apply(self, hero, enemy):
        hero.evade += 2
        hero.change_evade(hero.evade)
        print(f"{hero.name}'s evade chance increased to {round(hero.evade_percentage * 100, 1)}.'")

class HolyWater:
    cost = 15
    name = 'holy water'
    can_be_used = True
    def apply(self, hero, enemy):
        hero.holy_status = True
        print(f"{hero.name} is no longer afraid of the undying.")

class Lotto:
    cost = 1
    name = 'Lotto'
    can_be_used = False
    def apply(self, hero, enemy):
        lotto_ticket = random.randint(0, 1)
        if lotto_ticket == 0:
            print("Sorry. You lose.")
        else:
            hero.coins += lotto_ticket * 2
            print(f"You won! You get 2 coins.")

class Swap:
    cost = 10
    name = 'Swap potion'
    can_be_used = True
    def apply(self, hero, enemy):
        self.power = enemy.power
        print(f"You have swapped power with {enemy.name}")




class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade, HolyWater, Lotto, Swap]
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
