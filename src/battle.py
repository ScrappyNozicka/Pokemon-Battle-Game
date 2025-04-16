import random
from src.pokemon import Pokemon


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
        else:
            raise NoMoveError()

    def __select_action(self, action, move_name=None, new_pokemon=None):
        if action == "switch":
            self.__change_pokemon(new_pokemon)
            print(
                f"{'Player 1' if self.pokemon_1_turn else 'Player 2'} switched to {new_pokemon.name}"
            )
        elif action == "attack":
            pokemon = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
            if not move_name:
                move_name = pokemon.move.name
            move = self.__select_move(move_name)
            self.__pokemon_attack(move)
        else:
            raise ValueError(f"Unknown action: {action}")

    def __get_damage(self, move):
        attacker = self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        defender = self.pokemon_2 if self.pokemon_1_turn else self.pokemon_1
        critical_hit_success = random.randint(1, 20)
        critical_hit = 1
        if critical_hit_success == 20:
            critical_hit = 1.5
            print("Critical hit!")
        move_damage = move.attack_damage
        multiplier = attacker.get_multiplier(defender)
        damage = move_damage * multiplier * critical_hit
        return damage

    def __pokemon_attack(self, move):
        damage = self.__get_damage(move)
        if self.pokemon_1_turn:
            self.pokemon_2.take_damage(damage)
            print(f"{self.pokemon_2.name} has taken {damage} damage")
        else:
            self.pokemon_1.take_damage(damage)
            print(f"{self.pokemon_1.name} has taken {damage} damage")

    def take_turn(self, action="attack", move_name=None, new_pokemon=None):
        next_pokemon = (
            self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        )
        print(f"\nIt's {next_pokemon.name}'s turn!")
        self.__select_action(action, move_name, new_pokemon)
        self.pokemon_1_turn = not self.pokemon_1_turn

    def get_winner(self):
        while (
            not self.pokemon_1.has_fainted()
            and not self.pokemon_2.has_fainted()
        ):
            self.take_turn()
        if self.pokemon_1.has_fainted():
            fainted_pokemon = self.pokemon_1
            print(f"{fainted_pokemon.name} has fainted!")
            return self.pokemon_2
        else:
            fainted_pokemon = self.pokemon_2
            print(f"{fainted_pokemon.name} has fainted!")
            return self.pokemon_1

    def __str__(self):
        return (
            f"Battle between:\n"
            f"{self.pokemon_1.name}\n"
            f"{self.pokemon_2.name}\n"
            f"Next turn: {self.pokemon_1.name
                          if self.pokemon_1_turn
                          else self.pokemon_2.name}"
        )
