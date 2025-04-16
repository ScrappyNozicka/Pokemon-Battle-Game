from src.trainer import Trainer, NoEmptyPokeballError
from src.pokemon import Pokemon
from src.pokeball import Pokeball
import pytest


def test_trainer_has_empty_belt():
    test_trainer = Trainer("Scrooge")
    for pokeball in test_trainer.trainer_belt:
        assert type(pokeball) is Pokeball
    assert len(test_trainer.trainer_belt) == 6
    for pokeball in test_trainer.trainer_belt:
        assert pokeball.pokemon is None


def test_throw_pokeball_catches_pokemon_if_pokeballs_available():
    test_trainer = Trainer("Scrooge")
    test_pokemon = Pokemon("Bob", 3, 4, "move")
    test_trainer.throw_pokeball(test_pokemon)
    first_pokeball = test_trainer.trainer_belt[0]
    assert first_pokeball.pokemon == test_pokemon


def test_throw_pokeball_catches_multiple_pokemon_subsequently():
    test_trainer = Trainer("Scrooge")
    test_pokemon1 = Pokemon("Bob", 3, 4, "move")
    test_pokemon2 = Pokemon("Humphrey", 7, 4, "bash")
    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    first_pokeball = test_trainer.trainer_belt[0]
    second_pokeball = test_trainer.trainer_belt[1]
    assert first_pokeball.pokemon == test_pokemon1
    assert second_pokeball.pokemon == test_pokemon2


def test_throw_pokeball_catch_pokemon_while_some_pokemon_caught_already():
    test_pokemon1 = ("Bob", 3, 4, "move")
    test_trainer = Trainer("Scrooge")
    test_pokemon2 = Pokemon("Humphrey", 7, 4, "bash")
    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    first_pokeball = test_trainer.trainer_belt[0]
    assert first_pokeball.pokemon == test_pokemon1
    second_pokeball = test_trainer.trainer_belt[1]
    assert second_pokeball.pokemon == test_pokemon2


def test_throw_pokeball_does_not_catch_pokemon_if_no_available_pokeballs():
    test_pokemon1 = ("Bob", 3, 4, "move")
    test_pokemon2 = ("Humphrey", 7, 4, "bash")
    test_pokemon3 = ("Adalbert", 3, 3, "pokemon knowledge")
    test_pokemon4 = ("Redvers", 6, 8, "stuff")
    test_pokemon5 = ("Algernon", 2, 9, "bite")
    test_pokemon6 = ("Pancrazio", 5, 6, "gesturing")
    test_pokemon7 = ("Nebudchanezzar", 7, 4, "dreaming")
    test_trainer = Trainer("Scrooge")
    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    test_trainer.throw_pokeball(test_pokemon3)
    test_trainer.throw_pokeball(test_pokemon4)
    test_trainer.throw_pokeball(test_pokemon5)
    test_trainer.throw_pokeball(test_pokemon6)
    with pytest.raises(
        NoEmptyPokeballError, match="Sorry no empty pokeballs available"
    ):
        test_trainer.throw_pokeball(test_pokemon7)


def test_trainer_str_method_return_expected_output_when_all_empty_pokeballs():
    test_trainer = Trainer("Scrooge")
    expected_output = (
        "You have 0 pokemon's with you,\n" "you can catch 6 more."
    )
    assert str(test_trainer) == expected_output


def test_trainer_str_method_return_expected_output_when_all_some_pokeballs():
    test_pokemon1 = ("Bob", 3, 4, "move")
    test_pokemon2 = ("Humphrey", 7, 4, "bash")
    test_pokemon3 = ("Adalbert", 3, 3, "pokemon knowledge")
    test_trainer = Trainer("Scrooge")
    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    test_trainer.throw_pokeball(test_pokemon3)
    expected_output = (
        "You have 3 pokemon's with you,\n" "you can catch 3 more."
    )
    assert str(test_trainer) == expected_output


def test_trainer_str_method_return_expected_output_when_all_none_pokeballs():
    test_pokemon1 = ("Bob", 3, 4, "move")
    test_pokemon2 = ("Humphrey", 7, 4, "bash")
    test_pokemon3 = ("Adalbert", 3, 3, "pokemon knowledge")
    test_pokemon4 = ("Redvers", 6, 8, "stuff")
    test_pokemon5 = ("Algernon", 2, 9, "bite")
    test_pokemon6 = ("Pancrazio", 5, 6, "gesturing")
    test_trainer = Trainer("Scrooge")
    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    test_trainer.throw_pokeball(test_pokemon3)
    test_trainer.throw_pokeball(test_pokemon4)
    test_trainer.throw_pokeball(test_pokemon5)
    test_trainer.throw_pokeball(test_pokemon6)
    expected_output = (
        "You have 6 pokemon's with you,\n" "you can catch 0 more."
    )
    assert str(test_trainer) == expected_output
