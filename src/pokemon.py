class Pokemon:
    def __init__(
        self,
        name,
        hit_points,
        move_01,
        attack_damage_01,
        powerpoints_01,
        move_02,
        attack_damage_02,
        powerpoints_02,
        move_03,
        attack_damage_03,
        powerpoints_03,
    ):
        self.name = name
        self.hit_points = hit_points
        self.move_01 = move_01
        self.attack_damage_01 = attack_damage_01
        self.powerpoints_01 = powerpoints_01
        self.move_02 = move_02
        self.attack_damage_02 = attack_damage_02
        self.powerpoints_02 = powerpoints_02
        self.move_03 = move_03
        self.attack_damage_03 = attack_damage_03
        self.powerpoints_03 = powerpoints_03

    def use_move(self, move_number):
        if move_number == 1:
            return f"{self.name} used {self.move_01}"
        elif move_number == 2:
            return f"{self.name} used {self.move_02}"
        elif move_number == 3:
            return f"{self.name} used {self.move_03}"

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
    def __init__(
        self,
        name,
        hit_points,
        move_01,
        attack_damage_01,
        powerpoints_01,
        move_02,
        attack_damage_02,
        powerpoints_02,
        move_03,
        attack_damage_03,
        powerpoints_03,
    ):
        super().__init__(
            name,
            hit_points,
            move_01,
            attack_damage_01,
            powerpoints_01,
            move_02,
            attack_damage_02,
            powerpoints_02,
            move_03,
            attack_damage_03,
            powerpoints_03,
        )
        self.type = "Fire"
        self.strong_against = "Grass"
        self.weak_against = "Water"

    def __str__(self):
        return (
            f"{self.name} {self.type} type, HP: {self.hit_points},\n"
            f"Move: {self.move_01}, AP: {self.attack_damage_01}, PP: {self.powerpoints_01}\n"
            f"Move: {self.move_02}, AP: {self.attack_damage_02}, PP: {self.powerpoints_02}\n"
            f"Move: {self.move_03}, AP: {self.attack_damage_03}, PP: {self.powerpoints_03}"
        )


class WaterPokemon(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        move_01,
        attack_damage_01,
        powerpoints_01,
        move_02,
        attack_damage_02,
        powerpoints_02,
        move_03,
        attack_damage_03,
        powerpoints_03,
    ):
        super().__init__(
            name,
            hit_points,
            move_01,
            attack_damage_01,
            powerpoints_01,
            move_02,
            attack_damage_02,
            powerpoints_02,
            move_03,
            attack_damage_03,
            powerpoints_03,
        )
        self.type = "Water"
        self.strong_against = "Fire"
        self.weak_against = "Grass"

    def __str__(self):
        return (
            f"{self.name} {self.type} type, HP: {self.hit_points},\n"
            f"Move: {self.move_01}, AP: {self.attack_damage_01}, PP: {self.powerpoints_01}\n"
            f"Move: {self.move_02}, AP: {self.attack_damage_02}, PP: {self.powerpoints_02}\n"
            f"Move: {self.move_03}, AP: {self.attack_damage_03}, PP: {self.powerpoints_03}"
        )


class GrassPokemon(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        move_01,
        attack_damage_01,
        powerpoints_01,
        move_02,
        attack_damage_02,
        powerpoints_02,
        move_03,
        attack_damage_03,
        powerpoints_03,
    ):
        super().__init__(
            name,
            hit_points,
            move_01,
            attack_damage_01,
            powerpoints_01,
            move_02,
            attack_damage_02,
            powerpoints_02,
            move_03,
            attack_damage_03,
            powerpoints_03,
        )
        self.type = "Grass"
        self.strong_against = "Water"
        self.weak_against = "Fire"

    def __str__(self):
        return (
            f"{self.name} {self.type} type, HP: {self.hit_points},\n"
            f"Move: {self.move_01}, AP: {self.attack_damage_01}, PP: {self.powerpoints_01}\n"
            f"Move: {self.move_02}, AP: {self.attack_damage_02}, PP: {self.powerpoints_02}\n"
            f"Move: {self.move_03}, AP: {self.attack_damage_03}, PP: {self.powerpoints_03}"
        )


class NormalPokemon(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        move_01,
        attack_damage_01,
        powerpoints_01,
        move_02,
        attack_damage_02,
        powerpoints_02,
        move_03,
        attack_damage_03,
        powerpoints_03,
    ):
        super().__init__(
            name,
            hit_points,
            move_01,
            attack_damage_01,
            powerpoints_01,
            move_02,
            attack_damage_02,
            powerpoints_02,
            move_03,
            attack_damage_03,
            powerpoints_03,
        )
        self.type = "Normal"
        self.strong_against = None
        self.weak_against = None

    def __str__(self):
        return (
            f"{self.name} {self.type} type, HP: {self.hit_points},\n"
            f"Move: {self.move_01}, AP: {self.attack_damage_01}, PP: {self.powerpoints_01}\n"
            f"Move: {self.move_02}, AP: {self.attack_damage_02}, PP: {self.powerpoints_02}\n"
            f"Move: {self.move_03}, AP: {self.attack_damage_03}, PP: {self.powerpoints_03}"
        )
