class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move
        self.damage_taken = 0

    def use_move(self):
        return f"{self.name} used {self.move}"

    def take_damage(self, opponent_damage):
        self.damage_taken += opponent_damage
        return self.hit_points - self.damage_taken

    def has_fainted(self, opponent_damage):
        if self.hit_points <= self.damage_taken:
            return True
        else:
            return False

    def get_multiplier(self, opponent):
        if self.weak_against == opponent.type:
            return 0.5
        if self.strong_against == opponent.type:
            return 1.5
        if self.type is not opponent.strong_against or opponent.weak_against:
            return 1


class FirePokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "fire"
        self.strong_against = "grass"
        self.weak_against = "water"


class WaterPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "water"
        self.strong_against = "fire"
        self.weak_against = "grass"


class GrassPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "grass"
        self.strong_against = "water"
        self.weak_against = "fire"


class NormalPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "normal"
        self.strong_against = None
        self.weak_against = None
