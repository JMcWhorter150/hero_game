class Swap:
    cost = 5
    name = 'Swap trinket'
    can_be_used = True
    def apply(self, character):
        character.is_swapped = True