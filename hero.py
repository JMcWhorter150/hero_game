from character import Character
import time

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

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
