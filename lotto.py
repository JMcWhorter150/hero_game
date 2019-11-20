import random

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