from armor import Armor
from evade import Evade
from holywater import HolyWater
from lotto import Lotto
from supertonic import SuperTonic
from sword import Sword
from tonic import Tonic
from swap import Swap

class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade, HolyWater, Lotto, Swap]
    def do_shopping(self, hero, enemy):
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
            try:
                user_input = int(input("> "))
            except ValueError:
                print("Not a valid choice.")
                continue
            if user_input == 10:
                break
            else:
                try:
                    ItemToBuy = Store.items[user_input - 1]
                    item = ItemToBuy()
                    hero.buy(item, enemy)
                except IndexError:
                    print("Not a valid choice")