class Pokeball:
    """
    Represents a Pokeball that can hold a single Pokemon.

    Attributes:
        pokemon (Pokemon or None): 
            The Pokemon currently inside the Pokeball,
            or None if the Pokeball is empty.
    """

    def __init__(self):
        """
        Initializes an empty Pokeball.
        """
        self.pokemon = None

    def catch(self, encountered_pokemon):
        """
        Attempts to catch a Pokemon and store it in the Pokeball.

        Args:
            encountered_pokemon (Pokemon): The Pokemon to be caught.

        Prints:
            Success message if the Pokeball is empty and Pokemon is caught.
            Error message if the Pokeball is already full.
        """
        if self.pokemon is None:
            self.pokemon = encountered_pokemon
            print(f"{encountered_pokemon}" "Succesfully captured!")
        else:
            print("This pokeball is full.")

    def is_empty(self):
        """
        Checks if the Pokeball is empty.

        Returns:
            bool: True if the Pokeball is empty, False otherwise.
        """
        if self.pokemon is None:
            return True
        else:
            return False

    def contains_pokemon(self):
        """
        Alias for checking if the Pokeball contains a Pokemon.

        Returns:
            bool: True if a Pokemon is inside, False otherwise.
        """
        return self.pokemon is not None

    def __str__(self):
        """
        Returns a string representation of the Pokeball's state.

        Returns:
            str:
                Description of whether the Pokeball is empty
                    or what Pokemon it contains.
        """
        if not self.pokemon:
            return "This pokeball is empty and ready to be used."
        else:
            return f"This pokeball has {self.pokemon.name} in it."
