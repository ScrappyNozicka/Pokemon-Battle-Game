from move import Move


class Pokemon:
    def __init__(self, pokemon_id, name, hit_points, move_01, move_02, move_03):
        self.pokemon_id = pokemon_id
        self.name = name
        self.hit_points = hit_points
        self.moves = [move_01, move_02, move_03]

    def use_move(self, move_number):
        if 1 <= move_number <= len(self.moves):
            move = self.moves[move_number - 1]
            if move.use():
                return f"{self.name} used {move.name} (AP: {move.damage})"
            else:
                return f"{self.name} can't use {move.name}! Not enough PowerPoints."
        else:
            return f"{self.name} doesn't have that move."

    def take_damage(self, opponent_damage):
        self.hit_points -= opponent_damage
        return self.hit_points

    def has_fainted(self):
        if self.hit_points <= 0:
            return True
        else:
            return False

    def get_multiplier(self, opponent):
        if self.weak_against == opponent.type:
            return 0.5
        if self.strong_against == opponent.type:
            return 1.5
        else:
            return 1


class FirePokemon(Pokemon):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Fire"
        self.strong_against = "Grass"
        self.weak_against = "Water"

    def __str__(self):
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return f"{self.pokemon_id}: {self.name}, {self.type} type, HP: {self.hit_points}\n{move_details}\n"


class WaterPokemon(Pokemon):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Water"
        self.strong_against = "Fire"
        self.weak_against = "Grass"

    def __str__(self):
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return f"{self.pokemon_id}: {self.name}, {self.type} type, HP: {self.hit_points}\n{move_details}\n"


class GrassPokemon(Pokemon):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Grass"
        self.strong_against = "Water"
        self.weak_against = "Fire"

    def __str__(self):
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return f"{self.pokemon_id}: {self.name}, {self.type} type, HP: {self.hit_points}\n{move_details}\n"


class NormalPokemon(Pokemon):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Normal"
        self.strong_against = None
        self.weak_against = None

    def __str__(self):
        move_details = "\n".join(
            f"Move: {move.name}, AP: {move.damage}, PP: {move.powerpoints}"
            for move in self.moves
        )
        return f"{self.pokemon_id}: {self.name}, {self.type} type, HP: {self.hit_points}\n{move_details}\n"
