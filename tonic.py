class Tonic:
    cost = 5
    name = 'tonic'
    can_be_used = True
    potency = 2
    def apply(self, character):
        character.health += self.potency
        print("%s's health increased to %d." % (character.name, character.health))