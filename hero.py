from character import Character
import time
import random

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self.is_swapped = False

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def attack(self, enemy):
        if self.is_swapped:
            self.power, enemy.power = enemy.power, self.power
            print(f"{self.name} swaps power with {enemy.name}")
        if not self.is_alive(enemy):
            return
        print("%s attacks %s" % (self.name, enemy.name))
        critical_chance = random.randint(1, 5)
        if critical_chance > 4:
            enemy.receive_damage(self.power * 2)
            print(f"Critical hit! {self.name} did double damage to {enemy.name}")
        else: 
            enemy.receive_damage(self.power)
        if self.is_swapped:
            self.power, enemy.power = enemy.power, self.power
            self.is_swapped = False
        time.sleep(0.5)

    def buy(self, item, enemy):
        if self.coins < item.cost:
            print("Not enough coins.")
            return
        self.coins -= item.cost
        if item.can_be_used:    
            self.items.append(item)
        else:
            item.apply(self, enemy)

    def use_item(self, items, enemy):
        print("You have the following items:")
        for i in range(len(self.items)):
            print(f"{i}. {self.items[i].name}")
        choosing_item = True
        while choosing_item:
            print("Which item do you want to use? ")
            user_input = int(input("> "))
            if user_input in range(len(self.items)):
                self.items[user_input].apply(self)
                del self.items[user_input]
                choosing_item = False
            else:
                print("Invalid user input")
