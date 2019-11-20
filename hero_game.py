"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
import math
from hero import Hero
from battle import Battle
from goblin import Goblin
from medic import Medic
from sayan import Sayan
from shadow import Shadow
from store import Store
from thief import Thief
from wizard import Wizard
from zombie import Zombie

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
    shopping_engine.do_shopping(hero, enemy)

print("YOU WIN!")
