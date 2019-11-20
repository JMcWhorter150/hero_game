import time

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
                    try:
                        hero.use_item(hero.items, enemy)
                    except (ValueError, IndexError):
                        print("Did not choose an eligible item")
                        continue
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