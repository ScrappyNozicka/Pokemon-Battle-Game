import random
from utils_funcs import input_manager


class NoPokemonError(Exception):
    def __init__(self, message="This pokemon is not available"):
        super().__init__(message)


class NoMoveError(Exception):
    def __init__(self, message="This move is not available"):
        super().__init__(message)


class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.pokemon_1_turn = True

    def __change_pokemon(self, pokemon_to_change=None):
        if pokemon_to_change:
            if self.pokemon_1_turn is True:
                self.pokemon_1 = pokemon_to_change
                return self.pokemon_1
            else:
                self.pokemon_2 = pokemon_to_change
                return self.pokemon_2
        else:
            raise NoPokemonError()

    def __select_move(self, move_name):
        pokemon = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        for move in pokemon.moves:
            if move.name.lower() == move_name.lower():
                return move
        raise NoMoveError()

    def __select_action(self, action, move_name=None, new_pokemon=None):
        action = input_manager(
            "Please select action: "
            "[s]witch pokemon or [a]ttack and select move.\n"
        )
        if action == "s":
            new_pokemon = input_manager("Please select pokemon:")
            self.__change_pokemon(new_pokemon)
            print(
                f"{'Player 1' if self.pokemon_1_turn else 'Player 2'} switched to {new_pokemon.name}"
            )
        elif action == "a":
            move_name = input_manager("Please select move:")
            if not move_name:
                raise NoMoveError("No move name provided for attack action.")
            move = self.__select_move(move_name)
            self.__pokemon_attack(move)
        elif action not in "as":
            print(
                "Invalid action, please select valid action: "
                "[s]witch pokemon or [a]ttack and select move.\n"
            )
            self.__select_action()

    def __get_damage(self, move):
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
        attacker = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        move_result = attacker.use_move(attacker.moves.index(move) + 1)

        print(move_result)

        if "can't use" in move_result:
            return

        damage = self.__get_damage(move)
        defender = self.pokemon_2 if self.pokemon_1_turn else self.pokemon_1
        defender.take_damage(damage)
        print(f"{defender.name} has taken {damage} damage")

    def take_turn(self, action="attack", move_name=None, new_pokemon=None):
        while not self.__get_winner:
            next_pokemon = (
                self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
            )
            print(f"\nIt's {next_pokemon.name}'s turn!")
            self.__select_action(action, move_name, new_pokemon)
            self.pokemon_1_turn = not self.pokemon_1_turn

    def __get_winner(self):
        if self.pokemon_1.has_fainted():
            print(f"{self.pokemon_1.name} has fainted!")
            return True
        if self.pokemon_2.has_fainted():
            print(f"{self.pokemon_2.name} has fainted!")
            return True
        return False

    def __str__(self):
        return (
            f"Battle between:\n"
            f"{self.pokemon_1.name}\n"
            f"{self.pokemon_2.name}\n"
            f"Next turn: {self.pokemon_1.name
                          if self.pokemon_1_turn
                          else self.pokemon_2.name}"
        )
