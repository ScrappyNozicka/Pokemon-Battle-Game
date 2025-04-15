class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.pokemon_1_turn = True

    def __get_damage(self):
        if self.pokemon_1_turn:
            attacker = self.pokemon_1
            defender = self.pokemon_2
        else:
            attacker = self.pokemon_2
            defender = self.pokemon_1
        multiplier = attacker.get_multiplier(defender)
        damage = attacker.attack_damage * multiplier
        return damage

    def take_turn(self):
        next_pokemon = (
            self.pokemon_1 if self.pokemon_1_turn else self.pokemon_2
        )
        print(f"It's {next_pokemon.name} turn")      
        if self.pokemon_1_turn:
            self.pokemon_2.take_damage(self.__get_damage())
            print(
                f"{self.pokemon_2.name} has taken {self.__get_damage()} damage"
            )
        else:
            self.pokemon_1.take_damage(self.__get_damage())
            print(
                f"{self.pokemon_1.name} has taken {self.__get_damage()} damage"
            )
        self.pokemon_1_turn = not self.pokemon_1_turn

    def get_winner(self):
        while (
            not self.pokemon_1.has_fainted()
            and not self.pokemon_2.has_fainted()
        ):
            self.take_turn()
        if self.pokemon_1.has_fainted():
            winner = self.pokemon_2
            print(f"\n\n{winner.name} is the winner!!\n\n")
            return self.pokemon_2
        else:
            winner = self.pokemon_1
            print(f"\n\n{winner.name} is the winner!!\n\n")
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
