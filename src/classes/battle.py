import random
from src.utils.utils_funcs import input_manager


class NoPokemonError(Exception):
    """Exception raised when a Pokemon is not available or has fainted."""

    def __init__(self, message="This pokemon is not available"):
        super().__init__(message)


class Battle:
    """
    Represents a battle between two trainers and their selected Pokemon.

    Handles turn-based combat, move selection, Pokemon switching,
    damage calculation, and determining the winner.
    """

    def __init__(self, trainer_1, trainer_2, pokemon_1, pokemon_2):
        """
        Initialize the battle.

        Args:
            trainer_1 (Trainer): First trainer.
            trainer_2 (Trainer): Second trainer.
            pokemon_1 (Pokemon): Pokemon selected by trainer_1.
            pokemon_2 (Pokemon): Pokemon selected by trainer_2.
        """
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.pokemon_1_turn = True
        self.available_pokemon = [pokemon_1, pokemon_2]

    def __change_pokemon(self, pokemon_id_to_change=None):
        """
        Switch the current Pokemon with another from the trainer's belt.

        Args:
            pokemon_id_to_change (str): The ID of the new Pokemon.

        Returns:
            Pokemon: The new Pokemon selected.

        Raises:
            NoPokemonError: If the Pokemon ID is invalid or has fainted.
        """
        trainer = self.trainer_1 if self.pokemon_1_turn else self.trainer_2

        new_pokemon = trainer.get_pokemon_by_id(pokemon_id_to_change)
        if new_pokemon and not new_pokemon.has_fainted():
            if self.pokemon_1_turn:
                self.pokemon_1 = new_pokemon
            else:
                self.pokemon_2 = new_pokemon
            return new_pokemon
        else:
            raise NoPokemonError("Pokemon ID is invalid or unavailable.")

    def __force_switch(self, trainer):
        """
        Forces a trainer to switch Pokemon after one faints.

        Args:
            trainer (Trainer): Trainer whose Pokemon has fainted.

        Returns:
            Pokemon or None: Replacement Pokemon or None if none available.
        """
        print(f"{trainer.name}, your pokemon has fainted!")
        available = [
            p.pokemon
            for p in trainer.trainer_belt
            if not p.is_empty() and not p.pokemon.has_fainted()
        ]

        if not available:
            print(f"{trainer.name} has no more usable pokemon!")
            return None

        print(f"{trainer.name}'s available Pokemon:")
        for p in available:
            print(
                f"{p.pokemon_id}: {p.name}, Type: {p.type}, HP: {p.hit_points}"
            )

        while True:
            choice = input_manager(
                f"{trainer.name}, choose a replacement Pokemon by ID:"
            )
            selected = trainer.get_pokemon_by_id(choice)
            if selected and not selected.has_fainted():
                if trainer == self.trainer_1:
                    self.pokemon_1 = selected
                else:
                    self.pokemon_2 = selected
                print(f"{trainer.name} sent out {selected.name}!")
                return selected
            print("Invalid choice or that Pokemon has fainted. Try again.")

    def __select_move(self):
        """
        Prompts the trainer to select a move for their active Pokemon.
        Executes the selected move.
        """
        pokemon = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2

        print("Available moves:")
        for idx, move in enumerate(pokemon.moves, 1):
            print(
                f"{idx}. {move.name} (AP: {move.damage}, "
                f"PP: {move.powerpoints}/{move.max_powerpoints})"
            )

        while True:
            move_choice = input_manager("Select move by number:")

            if not move_choice.isdigit():
                print("Please enter a number.")
                continue

            move_index = int(move_choice) - 1

            if 0 <= move_index < len(pokemon.moves):
                move = pokemon.moves[move_index]
                self.__pokemon_attack(move)
                return move
            else:
                print("Invalid move number. Try again.")

    def __select_action(self):
        """
        Allows the trainer to choose an action: switch Pokemon or attack.
        """
        while True:
            action = input_manager(
                "Please select action: [s]witch pokemon "
                "or [a]ttack and select move.\n"
            ).lower()

            if action == "s":
                new_pokemon_id = input_manager("Please select pokemon id:")
                new_pokemon = self.__change_pokemon(new_pokemon_id)
                if new_pokemon:
                    print(
                        f"{self.trainer_1.name.capitalize()
                           if self.pokemon_1_turn
                           else self.trainer_2.name.capitalize()} "
                        f"switched to {new_pokemon.name}."
                    )
                    break

            elif action == "a":
                self.__select_move()
                break

            else:
                print("Invalid action. Please try again.")

    def __get_damage(self, move):
        """
        Calculates damage dealt by the given move,
        including multipliers and critical hits.

        Args:
            move (Move): The move being used.

        Returns:
            float: Calculated damage.
        """
        attacker = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        defender = self.pokemon_2 if self.pokemon_1_turn else self.pokemon_1
        critical_hit_success = random.randint(1, 20)
        critical_hit = 1
        if critical_hit_success == 20:
            critical_hit = 1.5
            print("Critical hit!")
        move_damage = move.damage
        multiplier = attacker.get_multiplier(defender)
        damage = move_damage * multiplier * critical_hit
        return damage

    def __pokemon_attack(self, move):
        """
        Executes an attack with the specified move
        and applies damage to the opposing Pokemon.

        Args:
            move (Move): The selected move to use.
        """
        attacker = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        defender = self.pokemon_2 if self.pokemon_1_turn else self.pokemon_1
        defender_trainer = (
            self.trainer_2 if self.pokemon_1_turn else self.trainer_1
        )

        move_result = attacker.use_move(attacker.moves.index(move) + 1)
        print(move_result)

        if "can't use" in move_result:
            return

        damage = self.__get_damage(move)
        defender.take_damage(damage)
        print(
            f"{defender.name} has taken {damage:.1f} damage "
            f"and has {defender.hit_points:.1f} HP left."
        )

        if defender.has_fainted():
            print(f"{defender.name} has fainted!")

            available = [
                pb.pokemon
                for pb in defender_trainer.trainer_belt
                if not pb.is_empty() and not pb.pokemon.has_fainted()
            ]

            if not available:
                print(f"{defender_trainer.name} has no Pokemon left!")
                return
            else:
                replacement = self.__force_switch(defender_trainer)
                if replacement:
                    print(
                        f"{defender_trainer.name} switched "
                        f"to {replacement.name}!"
                    )
                    return

    def take_turn(self):
        """
        Runs a full turn for both trainers until one wins the battle.

        Returns:
            Trainer: The winning trainer.
        """
        while not self.__get_winner():
            current_pokemon = (
                self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
            )

            print(f"\nIt's {current_pokemon.name}'s turn!")
            self.__select_action()

            defender = (
                self.pokemon_2 if self.pokemon_1_turn else self.pokemon_1
            )
            defending_trainer = (
                self.trainer_2 if self.pokemon_1_turn else self.trainer_1
            )

            if defender.has_fainted():
                print(f"{defender.name} has fainted!")
                replacement = self.__force_switch(defending_trainer)
                if not replacement:
                    break

            self.pokemon_1_turn = not self.pokemon_1_turn

        return (
            self.trainer_1
            if not any(
                p.pokemon and not p.pokemon.has_fainted()
                for p in self.trainer_2.trainer_belt
            )
            else self.trainer_2
        )

    def __get_winner(self):
        """
        Checks if the battle has a winner.

        Returns:
            bool: True if a Pokemon has fainted and the battle is over.
        """
        if self.pokemon_1.has_fainted():
            print(f"{self.pokemon_1.name} has fainted!")
            return True
        if self.pokemon_2.has_fainted():
            print(f"{self.pokemon_2.name} has fainted!")
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of the battle status.

        Returns:
            str: Current state of the battle.
        """
        return (
            f"Battle between:\n"
            f"{self.pokemon_1.name}\n"
            f"{self.pokemon_2.name}\n"
            f"Next turn: {self.pokemon_1.name
                          if self.pokemon_1_turn
                          else self.pokemon_2.name}"
        )
