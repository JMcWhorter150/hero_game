"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def print_status(self):
            print(f"{self.name} has {self.health} health and {self.power} power.")

# I want the status to print You have for hero
# I want the status to print X has for other characters

class Hero(Character):

    def is_alive(self):
        if self.health <= 0:
            print("You are dead.")
            return False
        else:
            return True

class Goblin(Character):
    
    def is_alive(self):
        if self.health <= 0:
            print("The goblin is dead.")
            return False
        else:
            return True

class Zombie(Character):
    def is_alive(self):
        return True
        
def main():
    hero = Hero("Hero", 10, 5)
    goblin = Goblin("Goblin", 6, 2)

    while goblin.is_alive() and hero.is_alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
            print("You do %d damage to the goblin." % hero.power)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)

def main2():
    zombie = Zombie("Zombie", 1, 1)
    hero = Hero("Hero", 10, 5)

    while zombie.is_alive() and hero.is_alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(zombie)
            print("You do %d damage to the zombie." % hero.power)
            if zombie.health <= 0:
                print("The zombie just won't die!")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        zombie.attack(hero)
        print("The zombie does %d damage to you." % zombie.power)

main()
# main2()
