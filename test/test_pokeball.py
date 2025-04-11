from src.pokeball import Pokeball


def test_pokeball_is_empty():
    test_pokeball = Pokeball()
    assert test_pokeball.pokemon is None


def test_pokeball_catch_pokemon_with_empty_pokeball():
    test_pokeball = Pokeball()
    test_pokeball.catch("Infernus")
    assert test_pokeball.pokemon == "Infernus"


def test_pokeball_catch_pokemon_with_full_pokeball():
    test_pokeball = Pokeball()
    test_pokeball.catch("Bob")
    test_pokeball.catch("Infernus")
    assert test_pokeball.pokemon == "Bob"


def test_pokeball_is_empty_with_empty_ball():
    test_pokeball = Pokeball()
    test_pokeball.is_empty()
    assert test_pokeball.is_empty() is True


def test_pokeball_is_empty_with_full_ball():
    test_pokeball = Pokeball()
    test_pokeball.catch("Infernus")
    test_pokeball.is_empty()
    assert test_pokeball.is_empty() is False
