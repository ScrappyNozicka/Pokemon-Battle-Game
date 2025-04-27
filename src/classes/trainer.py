from src.classes.pokeball import Pokeball


class NoEmptyPokeballError(Exception):
    """
    Custom exception raised when a trainer attempts to
    catch a Pokemon but has no empty Pokéballs.
    """

    def __init__(self, message="Sorry no empty pokeballs available"):
        super().__init__(message)


class Trainer:
    """
    Represents a Pokemon trainer who can
    carry and manage up to six Pokeballs on their belt.
    """

    def __init__(self, trainer_name):
        """
        Initializes a Trainer with a name, belt space and six empty Pokeballs.

        Args:
            trainer_name (str): The name of the trainer.
        """
        self.name = trainer_name
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
        """
        Attempts to catch a Pokemon using the first available empty Pokeball.

        Args:
            pokemon_in_nature (Pokemon): The wild Pokemon to catch.

        Raises:
            NoEmptyPokeballError: If there are no empty Pokeballs left.
        """
        if self.space_on_belt > 0:
            for pokeball in self.trainer_belt:
                if pokeball.is_empty():
                    pokeball.catch(pokemon_in_nature)
                    self.space_on_belt -= 1
                    return
        else:
            raise NoEmptyPokeballError()

    def get_pokemon_by_id(self, pokemon_id):
        """
        Retrieves a Pokemon from the trainer's belt by its ID.

        Args:
            pokemon_id (str): The ID of the Pokemon to retrieve.

        Returns:
            Pokemon or None: The Pokemon object if found, otherwise None.
        """
        for pokeball in self.trainer_belt:
            if pokeball.is_empty():
                continue
            if str(pokeball.pokemon.pokemon_id) == str(pokemon_id):
                return pokeball.pokemon
        return None

    def belt_space(self):
        """
        Checks if there is space on the trainer's belt for more Pokemon.

        Returns:
            bool: True if space is available, False otherwise.
        """
        if self.space_on_belt > 0:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a string representation of the trainer's current Pokeball use.

        Returns:
            str: A summary of how many Pokemon are caught and how many can be.
        """
        return (
            f"You have {6 - self.space_on_belt} pokemon's with you,\n"
            f"you can catch {self.space_on_belt} more."
        )
