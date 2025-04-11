from src.pokeball import Pokeball

# maybe make 6 child class pokeballs (is that even the right term)


class NoEmptyPokeballError(Exception):
    def __init__(self, message="Sorry no empty pokeballs available"):
        super().__init__(message)


# littlebenefitfromthesebeingseparateones
# atypicalforpythontoletclassesbekeys
class Trainer:

    def __init__(self, prefilled_pokemon=None):
        self.belt = [Pokeball() for _ in range(6)]
        if prefilled_pokemon:
            self.belt[0].catch(prefilled_pokemon)

    # Belt here isn't dynamic - doesn't need to be passed in

    def throw_pokeball(self, pokemon_in_nature):
        for index, pokeball in enumerate(self.belt):
            if pokeball.is_empty():
                pokeball.catch(pokemon_in_nature)
                break
        else:
            raise NoEmptyPokeballError()
