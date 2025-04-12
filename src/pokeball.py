class Pokeball:
    def __init__(self):
        self.pokemon = None

    def catch(self, encountered_pokemon):
        if self.pokemon is None:
            self.pokemon = encountered_pokemon
            print(f"{encountered_pokemon} succesfully captured!")
        else:
            print("This pokeball is full.")

    def is_empty(self):
        if self.pokemon is None:
            return True
        else:
            return False

    def __str__(self):
        if not self.pokemon:
            return "This pokeball is empty and ready to be used."
        else:
            return f"This pokeball has {self.pokemon} in it."
