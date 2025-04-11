from src.pokemon import Pokemon
from src.pokemon import FirePokemon
from src.pokemon import WaterPokemon
from src.pokemon import GrassPokemon
from src.pokemon import NormalPokemon


def test_pokemon_has_name():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")

    assert test_pokemon.name == "Bob"


def test_pokemon_has_hit_points():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")

    assert test_pokemon.hit_points == 500


def test_pokemon_has_attack_damage():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")

    assert test_pokemon.attack_damage == 1


def test_pokemon_has_move():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")

    assert test_pokemon.move == "slap"


def test_pokemon_used_move():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")
    test_pokemon.use_move()

    assert test_pokemon.use_move() == "Bob used slap"


def test_pokemon_take_damage():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")
    opponent_damage = 51
    assert test_pokemon.take_damage(opponent_damage) == 449


def test_pokemon_has_fainted():
    test_pokemon = Pokemon("Bob", 500, 1, "slap")
    opponent_damage = 100
    test_pokemon.take_damage(opponent_damage)
    test_pokemon.take_damage(opponent_damage)
    test_pokemon.take_damage(opponent_damage)
    test_pokemon.take_damage(opponent_damage)
    test_pokemon.take_damage(opponent_damage)
    test_pokemon.has_fainted(opponent_damage)
    assert test_pokemon.has_fainted(opponent_damage) is True


# test fire
def test_pokemon_fire_is_strong_against_grass_weak_against_water():
    test_pokemon = FirePokemon("Infernus", 30, 2, "flamethrow")
    assert test_pokemon.type == "fire"
    assert test_pokemon.strong_against == "grass"
    assert test_pokemon.weak_against == "water"


def test_pokemon_water_is_strong_against_fire_weak_against_grass():
    test_pokemon = WaterPokemon("Voda", 60, 5, "hurricane")
    assert test_pokemon.type == "water"
    assert test_pokemon.strong_against == "fire"
    assert test_pokemon.weak_against == "grass"


def test_pokemon_grass_is_strong_against_water_weak_against_fire():
    test_pokemon = GrassPokemon("Herbus", 45, 3, "grow")
    assert test_pokemon.type == "grass"
    assert test_pokemon.strong_against == "water"
    assert test_pokemon.weak_against == "fire"


def test_pokemon_normal_is_strong_and_weak_against_none():
    test_pokemon = NormalPokemon("Typicus", 10, 4, "complain")
    assert test_pokemon.type == "normal"
    assert test_pokemon.strong_against is None
    assert test_pokemon.weak_against is None


# get multiplier
def test_get_multiplier_returns_1point5_when_strong_against_passed_pokemon():
    test_pokemon = FirePokemon("Infernus", 30, 2, "flamethrow")

    opponent = GrassPokemon("Herbus", 45, 3, "grow")

    assert test_pokemon.get_multiplier(opponent) == 1.5


def test_get_multiplier_returns_0point5_when_weak_against_passed_pokemon():
    test_pokemon = WaterPokemon("Voda", 60, 5, "hurricane")

    opponent = GrassPokemon("Herbus", 45, 3, "grow")

    assert test_pokemon.get_multiplier(opponent) == 0.5


def test_get_multiplier_returns_1_when_neither_strong_nor_weak_against():
    test_pokemon = NormalPokemon("Typicus", 10, 4, "complain")

    opponent = GrassPokemon("Herbus", 45, 3, "grow")

    assert test_pokemon.get_multiplier(opponent) == 1
