from src.pokeball import Pokeball
from src.pokemon import FirePokemon, NormalPokemon
from src.move import Move


def test_pokeball_is_empty():
    test_pokeball = Pokeball()
    assert test_pokeball.pokemon is None


def test_pokeball_catch_pokemon_with_empty_pokeball():
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon)

    assert test_pokeball.pokemon.name == "Infernus"
    assert test_pokeball.pokemon == test_pokemon


def test_pokeball_catch_pokemon_with_full_pokeball():
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon_01 = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon_01)

    move4 = Move("Attackus", 10, 5)
    move5 = Move("Stronger Attackus", 15, 3)
    move6 = Move("Max Attackus", 20, 2)
    test_pokemon_02 = NormalPokemon("02", "Bob", 1, move4, move5, move6)

    test_pokeball.catch(test_pokemon_02)

    assert test_pokeball.pokemon.name == "Infernus"
    assert test_pokeball.pokemon == test_pokemon_01
    assert test_pokeball.pokemon.name != "Bob"
    assert test_pokeball.pokemon != test_pokemon_02


def test_pokeball_is_empty_with_empty_ball():
    test_pokeball = Pokeball()
    test_pokeball.is_empty()
    assert test_pokeball.is_empty() is True


def test_pokeball_is_empty_with_full_ball():
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon_01 = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon_01)

    test_pokeball.is_empty()

    assert test_pokeball.is_empty() is False


def test_pokeball_str_method_return_expected_output_when_empty():
    test_pokeball = Pokeball()

    expected_output = "This pokeball is empty and ready to be used."

    assert str(test_pokeball) == expected_output


def test_pokeball_str_method_return_expected_output_when_full():
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon_01 = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon_01)

    print(test_pokeball)

    expected_output = "This pokeball has Infernus in it."

    assert str(test_pokeball) == expected_output


def test_pokeball_contains_pokemon_return_expected_output_when_empty():
    test_pokeball = Pokeball()

    assert test_pokeball.contains_pokemon() is False


def test_pokeball_contains_pokemon_return_expected_output_when_full():
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon_01 = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon_01)

    assert test_pokeball.contains_pokemon() is True
