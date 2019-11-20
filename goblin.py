from character import Character

class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, 6, 0, 1, 2, 0, 5)