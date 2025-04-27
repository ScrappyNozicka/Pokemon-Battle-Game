from src.classes.move import Move
from src.classes.pokemon import (
    Pokemon,
    FirePokemon,
    WaterPokemon,
    GrassPokemon,
    NormalPokemon,
    ElectricPokemon,
    FightingPokemon,
    PoisonPokemon,
    PsychicPokemon,
    BugPokemon,
    GhostPokemon,
    DragonPokemon,
    FairyPokemon,
    GroundPokemon,
)


def test_pokemon_has_id():
    """
    Tests that the 'Pokemon' object correctly initializes
        and returns the pokemon ID.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    assert test_pokemon.pokemon_id == "01"


def test_pokemon_has_name():
    """
    Tests that the 'Pokemon' object correctly initializes
        and returns the pokemon name.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    assert test_pokemon.name == "Bob"


def test_pokemon_has_hit_points():
    """
    Tests that the 'Pokemon' object initializes
        with the correct hit points as an integer.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    assert type(test_pokemon.hit_points) is int
    assert test_pokemon.hit_points == 500


def test_pokemon_has_moves():
    """
    Tests that the 'Pokemon' object correctly initializes
        and returns a list of moves.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    assert type(test_pokemon.moves) is list
    assert test_pokemon.moves[0] == "Attack"
    assert test_pokemon.moves[1] == "Stronger Attack"
    assert test_pokemon.moves[2] == "Max Attack"
    assert test_pokemon.moves == ["Attack", "Stronger Attack", "Max Attack"]


def test_pokemon_used_move():
    """
    Tests that the 'Pokemon' object correctly uses a move
        and returns the expected string output.
    """
    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon = Pokemon("01", "Bob", 500, move1, move2, move3)
    test_move_num = 1

    assert test_pokemon.use_move(test_move_num) == "Bob used Attack (AP: 10)"


def test_pokemon_used_all_moves():
    """
    Tests that the 'Pokemon' object correctly uses all available moves
        and returns the expected output.
    """
    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon = Pokemon("01", "Bob", 500, move1, move2, move3)
    test_move_num_01 = 1
    test_move_num_02 = 2
    test_move_num_03 = 3

    assert (
        test_pokemon.use_move(test_move_num_01) == "Bob used Attack (AP: 10)"
    )
    assert (
        test_pokemon.use_move(test_move_num_02)
        == "Bob used Stronger Attack (AP: 15)"
    )
    assert (
        test_pokemon.use_move(test_move_num_03)
        == "Bob used Max Attack (AP: 20)"
    )


def test_pokemon_used_move_with_no_powerpoints():
    """
    Tests that the 'Pokemon' object correctly handles using a move
        with no power points (PP).
    """
    move1 = Move("Attack", 10, 0)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon = Pokemon("01", "Bob", 500, move1, move2, move3)
    test_move_num = 1

    assert (
        test_pokemon.use_move(test_move_num)
        == "Bob can't use Attack! Not enough PowerPoints."
    )


def test_pokemon_used_move_with_invalid_value():
    """
    Tests that the 'Pokemon' object returns the correct message
        when an invalid move index is provided.
    """
    move1 = Move("Attack", 10, 0)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon = Pokemon("01", "Bob", 500, move1, move2, move3)
    test_move_num = 4

    assert (
        test_pokemon.use_move(test_move_num) == "Bob doesn't have that move."
    )


def test_pokemon_take_damage_once_with_remaining_lives():
    """
    Tests that the 'Pokemon' object correctly calculates
        remaining hit points after taking damage.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    assert test_pokemon.take_damage(opponent_damage=51) == 449


def test_pokemon_take_damage_multi_times_with_remaining_lives():
    """
    Tests that the 'Pokemon' object correctly calculates
        remaining hit points after taking multiple instances of damage.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    test_pokemon.take_damage(opponent_damage=50)
    test_pokemon.take_damage(opponent_damage=100)
    assert test_pokemon.take_damage(opponent_damage=150) == 200


def test_pokemon_take_damage_returns_zero_if_damage_over_max_hp_received():
    """
    Tests that the 'Pokemon' object returns 0 hit points
        if the damage received exceeds the maximum hit points.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    assert test_pokemon.take_damage(opponent_damage=1000) == 0


def test_pokemon_has_not_fainted():
    """
    Tests that the 'Pokemon' object correctly returns False
        when the Pokemon has not fainted after taking damage.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    assert test_pokemon.has_fainted() is False


def test_pokemon_has_fainted():
    """
    Tests that the 'Pokemon' object correctly returns True
        when the Pokemon has fainted after taking sufficient damage.
    """
    test_pokemon = Pokemon(
        "01", "Bob", 500, "Attack", "Stronger Attack", "Max Attack"
    )

    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    test_pokemon.take_damage(opponent_damage=100)
    assert test_pokemon.has_fainted() is True


def test_normal_pokemon_str_method_return_expected_output_with_damage():
    """
    Tests that the string representation of a 'NormalPokemon' object
        returns the expected output when it has taken damage.
    """
    move1 = Move("Complain", 5, 10)
    move2 = Move("Call Manager", 15, 5)
    move3 = Move("Scratch", 10, 10)
    test_pokemon = NormalPokemon("05", "Typicus", 10, move1, move2, move3)

    test_pokemon.take_damage(opponent_damage=2)
    test_pokemon.take_damage(opponent_damage=2)

    expected_output = (
        "05: Typicus, Normal type, HP: 6\n"
        "Move: Complain, AP: 5, PP: 10\n"
        "Move: Call Manager, AP: 15, PP: 5\n"
        "Move: Scratch, AP: 10, PP: 10\n"
    )

    assert str(test_pokemon) == expected_output


def test_get_multiplier_returns_1point5_when_strong_against_passed_pokemon():
    """
    Tests that the 'get_multiplier' method correctly returns 1.5
        when the Pokemon is strong against the passed opponent.
    """
    test_pokemon = FirePokemon(
        "02", "Infernus", 30, "Flamethrow", "Ember", "Lavalamp"
    )

    opponent = GrassPokemon("03", "Herbus", 45, "Grow", "Bloom", "Thorn Whip")

    assert test_pokemon.get_multiplier(opponent) == 1.5


def test_get_multiplier_returns_0point5_when_weak_against_passed_pokemon():
    """
    Tests that the 'get_multiplier' method correctly returns 0.5
        when the Pokemon is weak against the passed opponent.
    """
    test_pokemon = WaterPokemon(
        "04", "Voda", 60, "Hurricane", "Surf", "Cowabunga"
    )

    opponent = GrassPokemon("03", "Herbus", 45, "Grow", "Bloom", "Thorn Whip")

    assert test_pokemon.get_multiplier(opponent) == 0.5


def test_get_multiplier_returns_1_when_neither_strong_nor_weak_against():
    """
    Tests that the 'get_multiplier' method correctly returns 1
        when the Pokemon neither has an advantage nor disadvantage
            against the passed opponent.
    """
    test_pokemon = NormalPokemon(
        "05", "Typicus", 10, "Complain", "Call Manager", "Scratch"
    )

    opponent = GrassPokemon("03", "Herbus", 45, "Grow", "Bloom", "Thorn Whip")

    assert test_pokemon.get_multiplier(opponent) == 1


def test_pokemon_fire_is_strong_against_grass_weak_against_water():
    """
    Tests that the 'FirePokemon' object has the correct type interactions
        for being strong against Grass and weak against Water.
    """
    test_pokemon = FirePokemon(
        "02", "Infernus", 30, "Flamethrow", "Ember", "Lavalamp"
    )
    assert test_pokemon.type == "Fire"
    assert test_pokemon.strong_against == "Grass"
    assert test_pokemon.weak_against == "Water"


def test_fire_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'FirePokemon' object
        returns the expected output.
    """
    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon = FirePokemon("02", "Infernus", 30, move1, move2, move3)
    expected_output = (
        "02: Infernus, Fire type, HP: 30\n"
        "Move: Flamethrow, AP: 10, PP: 10\n"
        "Move: Ember, AP: 15, PP: 3\n"
        "Move: Lavalamp, AP: 20, PP: 2\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_water_is_strong_against_fire_weak_against_grass():
    """
    Tests that the 'WaterPokemon' object has the correct type interactions
        for being strong against Fire and weak against Grass.
    """
    test_pokemon = WaterPokemon(
        "04", "Voda", 60, "Hurricane", "Surf", "Cowabunga"
    )

    assert test_pokemon.type == "Water"
    assert test_pokemon.strong_against == "Fire"
    assert test_pokemon.weak_against == "Grass"


def test_water_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'WaterPokemon' object
        returns the expected output.
    """
    move1 = Move("Hurricane", 10, 5)
    move2 = Move("Surf", 15, 10)
    move3 = Move("Cowabunga", 20, 5)
    test_pokemon = WaterPokemon("04", "Voda", 60, move1, move2, move3)
    expected_output = (
        "04: Voda, Water type, HP: 60\n"
        "Move: Hurricane, AP: 10, PP: 5\n"
        "Move: Surf, AP: 15, PP: 10\n"
        "Move: Cowabunga, AP: 20, PP: 5\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_grass_is_strong_against_water_weak_against_fire():
    """
    Tests that the 'GrassPokemon' object has the correct type interactions
        for being strong against Water and weak against Fire.
    """
    test_pokemon = GrassPokemon(
        "03", "Herbus", 45, "Grow", "Bloom", "Thorn Whip"
    )
    assert test_pokemon.type == "Grass"
    assert test_pokemon.strong_against == "Water"
    assert test_pokemon.weak_against == "Fire"


def test_grass_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'GrassPokemon' object
        returns the expected output.
    """
    move1 = Move("Grow", 10, 10)
    move2 = Move("Bloom", 13, 8)
    move3 = Move("Thorn Whip", 16, 6)
    test_pokemon = GrassPokemon("03", "Herbus", 45, move1, move2, move3)
    expected_output = (
        "03: Herbus, Grass type, HP: 45\n"
        "Move: Grow, AP: 10, PP: 10\n"
        "Move: Bloom, AP: 13, PP: 8\n"
        "Move: Thorn Whip, AP: 16, PP: 6\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_normal_is_strong_and_weak_against_none():
    """
    Tests that the 'NormalPokemon' object has the correct type interactions
        for being strong against None and weak against None.
    """
    test_pokemon = NormalPokemon(
        "05", "Typicus", 10, "Complain", "Call Manager", "Scratch"
    )
    assert test_pokemon.type == "Normal"
    assert test_pokemon.strong_against is None
    assert test_pokemon.weak_against is None


def test_normal_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'NormalPokemon' object
        returns the expected output.
    """
    move1 = Move("Complain", 5, 10)
    move2 = Move("Call Manager", 15, 5)
    move3 = Move("Scratch", 10, 10)
    test_pokemon = NormalPokemon("05", "Typicus", 10, move1, move2, move3)
    expected_output = (
        "05: Typicus, Normal type, HP: 10\n"
        "Move: Complain, AP: 5, PP: 10\n"
        "Move: Call Manager, AP: 15, PP: 5\n"
        "Move: Scratch, AP: 10, PP: 10\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_electric_is_strong_against_water_and_weak_against_ground():
    """
    Tests that the 'ElectricPokemon' object has the correct type interactions
        for being strong against Water and weak against Ground.
    """
    test_pokemon = ElectricPokemon(
        "06", "Sparky", 10, "Thunder", "Lighting", "Lightbulb"
    )
    assert test_pokemon.type == "Electric"
    assert test_pokemon.strong_against == "Water"
    assert test_pokemon.weak_against == "Ground"


def test_electric_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'ElectricPokemon' object
        returns the expected output.
    """
    move1 = Move("Thunder", 2, 10)
    move2 = Move("Lighting", 10, 10)
    move3 = Move("Lightbulb", 12, 15)
    test_pokemon = ElectricPokemon("06", "Sparky", 50, move1, move2, move3)
    expected_output = (
        "06: Sparky, Electric type, HP: 50\n"
        "Move: Thunder, AP: 2, PP: 10\n"
        "Move: Lighting, AP: 10, PP: 10\n"
        "Move: Lightbulb, AP: 12, PP: 15\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_fighting_is_strong_against_normal_and_weak_against_flying():
    """
    Tests that the 'FightingPokemon' object has the correct type interactions
        for being strong against Normal and weak against Flying.
    """
    test_pokemon = FightingPokemon(
        "07", "One-Puncher", 10, "Light Punch", "Light Kick", "Fatal Punch"
    )
    assert test_pokemon.type == "Fighting"
    assert test_pokemon.strong_against == "Normal"
    assert test_pokemon.weak_against == "Flying"


def test_fighting_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'FightingPokemon' object
        returns the expected output.
    """
    move1 = Move("Light Punch", 10, 15)
    move2 = Move("Light Kick", 15, 10)
    move3 = Move("Fatal Punch", 20, 5)
    test_pokemon = FightingPokemon(
        "07", "One-Puncher", 75, move1, move2, move3
    )
    expected_output = (
        "07: One-Puncher, Fighting type, HP: 75\n"
        "Move: Light Punch, AP: 10, PP: 15\n"
        "Move: Light Kick, AP: 15, PP: 10\n"
        "Move: Fatal Punch, AP: 20, PP: 5\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_poison_is_strong_against_fairy_and_weak_against_psychic():
    """
    Tests that the 'PoisonPokemon' object has the correct type interactions
        for being strong against Fairy and weak against Psychic.
    """
    test_pokemon = PoisonPokemon(
        "08", "Foxglove", 45, "Irregular", "Sting", "Sleep"
    )
    assert test_pokemon.type == "Poison"
    assert test_pokemon.strong_against == "Fairy"
    assert test_pokemon.weak_against == "Psychic"


def test_poison_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'PoisonPokemon' object
        returns the expected output.
    """
    move1 = Move("Irregular", 15, 12)
    move2 = Move("Sting", 12, 20)
    move3 = Move("Sleep", 8, 35)
    test_pokemon = PoisonPokemon("08", "Foxglove", 45, move1, move2, move3)
    expected_output = (
        "08: Foxglove, Poison type, HP: 45\n"
        "Move: Irregular, AP: 15, PP: 12\n"
        "Move: Sting, AP: 12, PP: 20\n"
        "Move: Sleep, AP: 8, PP: 35\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_psychic_is_strong_against_fighting_and_weak_against_bug():
    """
    Tests that the 'PsychicPokemon' object has the correct type interactions
        for being strong against Fighting and weak against Bug.
    """
    test_pokemon = PsychicPokemon(
        "09", "Shazam", 30, "Psybeam", "Telekinesis", "Spoon Bending"
    )
    assert test_pokemon.type == "Psychic"
    assert test_pokemon.strong_against == "Fighting"
    assert test_pokemon.weak_against == "Bug"


def test_psychic_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'PsychicPokemon' object
        returns the expected output.
    """
    move1 = Move("Psybeam", 10, 25)
    move2 = Move("Telekinesis", 15, 15)
    move3 = Move("Spoon Bending", 25, 2)
    test_pokemon = PsychicPokemon("09", "Shazam", 30, move1, move2, move3)
    expected_output = (
        "09: Shazam, Psychic type, HP: 30\n"
        "Move: Psybeam, AP: 10, PP: 25\n"
        "Move: Telekinesis, AP: 15, PP: 15\n"
        "Move: Spoon Bending, AP: 25, PP: 2\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_bug_is_strong_against_psychic_and_weak_against_fire():
    """
    Tests that the 'BugPokemon' object has the correct type interactions
        for being strong against Psychic and weak against Fire.
    """
    test_pokemon = BugPokemon(
        "10", "Mantis", 44, "Cut", "Gossamer", "Bug Bite"
    )
    assert test_pokemon.type == "Bug"
    assert test_pokemon.strong_against == "Psychic"
    assert test_pokemon.weak_against == "Fire"


def test_bug_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'BugPokemon' object
        returns the expected output.
    """
    move1 = Move("Cut", 15, 10)
    move2 = Move("Gossamer", 20, 5)
    move3 = Move("Bug Bite", 10, 25)
    test_pokemon = BugPokemon("10", "Mantis", 44, move1, move2, move3)
    expected_output = (
        "10: Mantis, Bug type, HP: 44\n"
        "Move: Cut, AP: 15, PP: 10\n"
        "Move: Gossamer, AP: 20, PP: 5\n"
        "Move: Bug Bite, AP: 10, PP: 25\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_ghost_is_strong_against_psychic_and_weak_against_ghost():
    """
    Tests that the 'GhostPokemon' object has the correct type interactions
        for being strong against Psychic and weak against Ghost.
    """
    test_pokemon = GhostPokemon(
        "11", "Casper", 100, "Scream", "Scary Face", "Darklight"
    )
    assert test_pokemon.type == "Ghost"
    assert test_pokemon.strong_against == "Psychic"
    assert test_pokemon.weak_against == "Ghost"


def test_ghost_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'GhostPokemon' object
        returns the expected output.
    """
    move1 = Move("Scream", 10, 15)
    move2 = Move("Scary Face", 5, 35)
    move3 = Move("Darklight", 12, 20)
    test_pokemon = GhostPokemon("11", "Casper", 100, move1, move2, move3)
    expected_output = (
        "11: Casper, Ghost type, HP: 100\n"
        "Move: Scream, AP: 10, PP: 15\n"
        "Move: Scary Face, AP: 5, PP: 35\n"
        "Move: Darklight, AP: 12, PP: 20\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_dragon_is_strong_against_dragon_and_weak_against_ice():
    """
    Tests that the 'DragonPokemon' object has the correct type interactions
        for being strong against Dragon and weak against Ice.
    """
    test_pokemon = DragonPokemon(
        "12", "Mushu", 80, "Dragon Claw", "Roar", "Wing Slam"
    )
    assert test_pokemon.type == "Dragon"
    assert test_pokemon.strong_against == "Dragon"
    assert test_pokemon.weak_against == "Ice"


def test_dragon_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'DragonPokemon' object
        returns the expected output.
    """
    move1 = Move("Dragon Claw", 15, 10)
    move2 = Move("Roar", 10, 35)
    move3 = Move("Wing Slam", 20, 5)
    test_pokemon = DragonPokemon("12", "Mushu", 80, move1, move2, move3)
    expected_output = (
        "12: Mushu, Dragon type, HP: 80\n"
        "Move: Dragon Claw, AP: 15, PP: 10\n"
        "Move: Roar, AP: 10, PP: 35\n"
        "Move: Wing Slam, AP: 20, PP: 5\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_fairy_is_strong_against_dragon_and_weak_against_ice():
    """
    Tests that the 'FairyPokemon' object has the correct type interactions
        for being strong against Dragon and weak against Steel.
    """
    test_pokemon = FairyPokemon(
        "13", "Oberon", 50, "Fairy Dust", "Dreaming", "Fairytales"
    )
    assert test_pokemon.type == "Fairy"
    assert test_pokemon.strong_against == "Dragon"
    assert test_pokemon.weak_against == "Steel"


def test_fairy_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'FairyPokemon' object
        returns the expected output.
    """
    move1 = Move("Fairy Dust", 10, 30)
    move2 = Move("Dreaming", 12, 25)
    move3 = Move("Fairytales", 14, 20)
    test_pokemon = FairyPokemon("13", "Oberon", 50, move1, move2, move3)
    expected_output = (
        "13: Oberon, Fairy type, HP: 50\n"
        "Move: Fairy Dust, AP: 10, PP: 30\n"
        "Move: Dreaming, AP: 12, PP: 25\n"
        "Move: Fairytales, AP: 14, PP: 20\n"
    )
    assert str(test_pokemon) == expected_output


def test_pokemon_ground_is_strong_against_dragon_and_weak_against_ice():
    """
    Tests that the 'GroundPokemon' object has the correct type interactions
        for being strong against Fire and weak against Water.
    """
    test_pokemon = GroundPokemon(
        "14", "Sandworm", 45, "Tunnel", "Devour", "Sandstorm"
    )
    assert test_pokemon.type == "Ground"
    assert test_pokemon.strong_against == "Fire"
    assert test_pokemon.weak_against == "Water"


def test_ground_pokemon_str_method_return_expected_output():
    """
    Tests that the string representation of a 'GroundPokemon' object
        returns the expected output.
    """
    move1 = Move("Tunnel", 15, 15)
    move2 = Move("Devour", 10, 30)
    move3 = Move("Sandstorm", 25, 5)
    test_pokemon = GroundPokemon("14", "Sandworm", 45, move1, move2, move3)
    expected_output = (
        "14: Sandworm, Ground type, HP: 45\n"
        "Move: Tunnel, AP: 15, PP: 15\n"
        "Move: Devour, AP: 10, PP: 30\n"
        "Move: Sandstorm, AP: 25, PP: 5\n"
    )
    assert str(test_pokemon) == expected_output
