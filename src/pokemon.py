class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move

    def use_move(self):
        return f"{self.name} used {self.move}"

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
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "fire"
        self.strong_against = "grass"
        self.weak_against = "water"

    def __str__(self):
        return (
            f"{self.name} {self.type} type,\n"
            f"HP: {self.hit_points}, AP: {self.attack_damage},\n"
            f"Move: {self.move}"
        )


class WaterPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "water"
        self.strong_against = "fire"
        self.weak_against = "grass"

    def __str__(self):
        return (
            f"{self.name} {self.type} type,\n"
            f"HP: {self.hit_points}, AP: {self.attack_damage},\n"
            f"Move: {self.move}"
        )


class GrassPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "grass"
        self.strong_against = "water"
        self.weak_against = "fire"

    def __str__(self):
        return (
            f"{self.name} {self.type} type,\n"
            f"HP: {self.hit_points}, AP: {self.attack_damage},\n"
            f"Move: {self.move}"
        )


class NormalPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "normal"
        self.strong_against = None
        self.weak_against = None

    def __str__(self):
        return (
            f"{self.name} {self.type} type,\n"
            f"HP: {self.hit_points}, AP: {self.attack_damage},\n"
            f"Move: {self.move}"
        )
