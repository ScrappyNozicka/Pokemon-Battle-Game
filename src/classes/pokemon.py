class Pokemon:
    """
    Base class representing a generic Pokemon.

    Attributes:
        pokemon_id (str): Unique identifier of the Pokemon.
        name (str): Name of the Pokemon.
        hit_points (int): Current health of the Pokemon.
        moves (list): List of the Pokemon's 3 moves.
    """

    def __init__(
        self, pokemon_id, name, hit_points, move_01, move_02, move_03
    ):
        """
        Initialize a Pokemon with ID, name, HP, and 3 moves.

        Args:
            pokemon_id (str or int): The Pokemon's ID.
            name (str): The Pokemon's name.
            hit_points (int): The initial hit points.
            move_01, move_02, move_03 (Move): The Pokemon's 3 moves.
        """
        self.pokemon_id = pokemon_id
        self.name = name
        self.hit_points = hit_points
        self.moves = [move_01, move_02, move_03]

    def use_move(self, move_number):
        """
        Executes a move if the selected move number is valid
            and has PowerPoints.

        Args:
            move_number (int): The move number (1-3).

        Returns:
            str: Outcome message of using the move.
        """
        if 1 <= move_number <= len(self.moves):
            move = self.moves[move_number - 1]
            if move.use():
                return f"{self.name} used {move.name} (AP: {move.damage})"
            else:
                return (
                    f"{self.name} can't use {move.name}! "
                    "Not enough PowerPoints."
                )
        else:
            return f"{self.name} doesn't have that move."

    def take_damage(self, opponent_damage):
        """
        Applies damage to the Pokemon and reduces HP, without going below 0.

        Args:
            opponent_damage (int): Amount of damage taken.

        Returns:
            int: Updated HP after damage.
        """
        self.hit_points = max(0, self.hit_points - opponent_damage)
        return self.hit_points

    def has_fainted(self):
        """
        Checks if the Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, else False.
        """
        if self.hit_points <= 0:
            return True
        else:
            return False

    def get_multiplier(self, opponent):
        """
        Calculates the effectiveness multiplier based on opponent's type.

        Args:
            opponent (Pokemon): The opposing Pokemon.

        Returns:
            float: Multiplier (0.5 if weak, 1.5 if strong, 1 otherwise).
        """
        if self.weak_against == opponent.type:
            return 0.5
        if self.strong_against == opponent.type:
            return 1.5
        else:
            return 1


class FirePokemon(Pokemon):
    def __init__(self, *args):
        """Fire type Pokemon.
        Strong against Grass, weak against Water."""
        super().__init__(*args)
        self.type = "Fire"
        self.strong_against = "Grass"
        self.weak_against = "Water"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class WaterPokemon(Pokemon):
    def __init__(self, *args):
        """Water type Pokemon.
        Strong against Fire, weak against Grass."""
        super().__init__(*args)
        self.type = "Water"
        self.strong_against = "Fire"
        self.weak_against = "Grass"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class GrassPokemon(Pokemon):
    def __init__(self, *args):
        """Grass type Pokemon.
        Strong against Water, weak against Fire."""
        super().__init__(*args)
        self.type = "Grass"
        self.strong_against = "Water"
        self.weak_against = "Fire"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class NormalPokemon(Pokemon):
    def __init__(self, *args):
        """Normal type Pokemon.
        Strong against None, weak against None."""
        super().__init__(*args)
        self.type = "Normal"
        self.strong_against = None
        self.weak_against = None

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class ElectricPokemon(Pokemon):
    def __init__(self, *args):
        """Electric type Pokemon.
        Strong against Water, weak against Ground."""
        super().__init__(*args)
        self.type = "Electric"
        self.strong_against = "Water"
        self.weak_against = "Ground"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class FightingPokemon(Pokemon):
    def __init__(self, *args):
        """Fighting type Pokemon.
        Strong against Normal, weak against Flying."""
        super().__init__(*args)
        self.type = "Fighting"
        self.strong_against = "Normal"
        self.weak_against = "Flying"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class PoisonPokemon(Pokemon):
    def __init__(self, *args):
        """Poison type Pokemon.
        Strong against Fairy, weak against Psychic."""
        super().__init__(*args)
        self.type = "Poison"
        self.strong_against = "Fairy"
        self.weak_against = "Psychic"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class PsychicPokemon(Pokemon):
    def __init__(self, *args):
        """Psychic type Pokemon.
        Strong against Fighting, weak against Bug."""
        super().__init__(*args)
        self.type = "Psychic"
        self.strong_against = "Fighting"
        self.weak_against = "Bug"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class BugPokemon(Pokemon):
    def __init__(self, *args):
        """Bug type Pokemon.
        Strong against Psychic, weak against Fire."""
        super().__init__(*args)
        self.type = "Bug"
        self.strong_against = "Psychic"
        self.weak_against = "Fire"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class GhostPokemon(Pokemon):
    def __init__(self, *args):
        """Ghost type Pokemon. Strong against Psychic, weak against Ghost."""
        super().__init__(*args)
        self.type = "Ghost"
        self.strong_against = "Psychic"
        self.weak_against = "Ghost"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class DragonPokemon(Pokemon):
    def __init__(self, *args):
        """Dragon type Pokemon.
        Strong against Dragon, weak against Ice."""
        super().__init__(*args)
        self.type = "Dragon"
        self.strong_against = "Dragon"
        self.weak_against = "Ice"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class FairyPokemon(Pokemon):
    def __init__(self, *args):
        """Fairy type Pokemon.
        Strong against Dragon, weak against Steel."""
        super().__init__(*args)
        self.type = "Fairy"
        self.strong_against = "Dragon"
        self.weak_against = "Steel"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )


class GroundPokemon(Pokemon):
    def __init__(self, *args):
        """Ground type Pokemon.
        Strong against Fire, weak against Water."""
        super().__init__(*args)
        self.type = "Ground"
        self.strong_against = "Fire"
        self.weak_against = "Water"

    def __str__(self):
        """Returns formatted string with stats and moves."""
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return (
            f"{self.pokemon_id}: {self.name}, "
            f"{self.type} type, HP: {self.hit_points}\n"
            f"{move_details}\n"
        )
