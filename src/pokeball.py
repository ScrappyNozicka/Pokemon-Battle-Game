class Pokeball:
    def __init__(self):
        self.Pokemon = None

    def catch(self, encountered_pokemon):
        if self.Pokemon is None:
            self.Pokemon = encountered_pokemon
        else:
            print("This pokeball is full")

    def is_empty(self):
        if self.Pokemon is None:
            return True
        else:
            return False
