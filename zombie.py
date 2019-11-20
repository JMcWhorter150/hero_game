from character import Character

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