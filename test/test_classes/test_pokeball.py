from src.classes.pokeball import Pokeball
from src.classes.pokemon import FirePokemon, NormalPokemon
from src.classes.move import Move


def test_pokeball_is_empty():
    """
    Test that verifies if a newly created Pokeball is empty.
    Ensures that the Pokeball's 'pokemon' attribute
        is initially set to None.
    """
    test_pokeball = Pokeball()
    assert test_pokeball.pokemon is None


def test_pokeball_catch_pokemon_with_empty_pokeball():
    """
    Test that verifies if a Pokeball can catch a Pokemon
        when the Pokeball is empty.
    It checks if the 'pokemon' attribute of the Pokeball
        correctly stores the caught Pokemon.
    """
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon)

    assert test_pokeball.pokemon.name == "Infernus"
    assert test_pokeball.pokemon == test_pokemon


def test_pokeball_catch_pokemon_with_full_pokeball():
    """
    Test that verifies if a Pokeball, which already contains a Pokemon,
        will not catch a new Pokemon.
    It ensures the first Pokemon is retained.
    """
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
    """
    Test that verifies the 'is_empty' method of a Pokeball
        when the Pokeball is empty.
    It checks if the method returns True when no Pokemon is stored.
    """
    test_pokeball = Pokeball()
    test_pokeball.is_empty()
    assert test_pokeball.is_empty() is True


def test_pokeball_is_empty_with_full_ball():
    """
    Test that verifies the 'is_empty' method of a Pokeball
        when the Pokeball contains a Pokemon.
    It checks if the method returns False
        when a Pokemon is caught in the Pokeball.
    """
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon_01 = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon_01)

    test_pokeball.is_empty()

    assert test_pokeball.is_empty() is False


def test_pokeball_str_method_return_expected_output_when_empty():
    """
    Test the string representation of an empty Pokeball.
    It checks if the string output correctly reflects
        that the Pokeball is empty and ready to be used.
    """
    test_pokeball = Pokeball()

    expected_output = "This pokeball is empty and ready to be used."

    assert str(test_pokeball) == expected_output


def test_pokeball_str_method_return_expected_output_when_full():
    """
    Test the string representation of a full Pokeball.
    It checks if the string output correctly reflects
        that the Pokeball contains a Pokemon.
    """
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
    """
    Test the 'contains_pokemon' method of a Pokeball
        when it is empty.
    It checks if the method correctly returns False
        when no Pokemon is stored in the Pokeball.
    """
    test_pokeball = Pokeball()

    assert test_pokeball.contains_pokemon() is False


def test_pokeball_contains_pokemon_return_expected_output_when_full():
    """
    Test the 'contains_pokemon' method of a Pokeball
        when it contains a Pokemon.
    It checks if the method correctly returns True
        when a Pokemon is stored in the Pokeball.
    """
    test_pokeball = Pokeball()

    move1 = Move("Attack", 10, 5)
    move2 = Move("Stronger Attack", 15, 3)
    move3 = Move("Max Attack", 20, 2)
    test_pokemon_01 = FirePokemon("01", "Infernus", 1, move1, move2, move3)

    test_pokeball.catch(test_pokemon_01)

    assert test_pokeball.contains_pokemon() is True
