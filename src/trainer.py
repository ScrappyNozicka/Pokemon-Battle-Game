from src.pokeball import Pokeball


class NoEmptyPokeballError(Exception):
    def __init__(self, message="Sorry no empty pokeballs available"):
        super().__init__(message)


class Trainer:

    def __init__(self):
        self.pokeball_01 = Pokeball()
        self.pokeball_02 = Pokeball()
        self.pokeball_03 = Pokeball()
        self.pokeball_04 = Pokeball()
        self.pokeball_05 = Pokeball()
        self.pokeball_06 = Pokeball()
        self.trainer_belt = [
            self.pokeball_01,
            self.pokeball_02,
            self.pokeball_03,
            self.pokeball_04,
            self.pokeball_05,
            self.pokeball_06,
        ]
        self.space_on_belt = 6

    def throw_pokeball(self, pokemon_in_nature):
        if self.space_on_belt > 0:
            for pokeball in self.trainer_belt:
                if pokeball.is_empty():
                    pokeball.catch(pokemon_in_nature)
                    self.space_on_belt -= 1
                    return
            raise NoEmptyPokeballError()
