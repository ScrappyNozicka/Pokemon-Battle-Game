from src.classes.trainer import Trainer, NoEmptyPokeballError
from src.classes.pokemon import (
    NormalPokemon,
    ElectricPokemon,
    PoisonPokemon,
    GrassPokemon,
    FightingPokemon,
    WaterPokemon,
    FirePokemon,
)
from src.classes.pokeball import Pokeball
from src.classes.move import Move
import pytest


def test_trainer_has_empty_belt():
    """
    Test that a new trainer's belt is initialized with 6 empty Pokeballs.
    Each Pokeball should be of type Pokeball, and the pokemon inside each
        Pokeball should be None.
    """
    test_trainer = Trainer("Scrooge")

    for pokeball in test_trainer.trainer_belt:
        assert type(pokeball) is Pokeball

    assert len(test_trainer.trainer_belt) == 6

    for pokeball in test_trainer.trainer_belt:
        assert pokeball.pokemon is None


def test_throw_pokeball_catches_pokemon_if_pokeballs_available():
    """
    Test that a trainer can successfully catch a Pokemon when there is space
    in the Pokeballs. The first Pokeball in the trainer's belt should contain
        the caught Pokemon.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Complain", 5, 10)
    move2 = Move("Call Manager", 15, 5)
    move3 = Move("Scratch", 10, 10)
    test_pokemon = NormalPokemon("05", "Typicus", 10, move1, move2, move3)

    test_trainer.throw_pokeball(test_pokemon)

    first_pokeball = test_trainer.trainer_belt[0]

    assert first_pokeball.pokemon == test_pokemon


def test_throw_pokeball_catches_multiple_pokemon_subsequently():
    """
    Test that a trainer can catch multiple Pokemon subsequently, with each
    Pokemon being placed in the next available Pokeball in the trainer's belt.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Complain", 5, 10)
    move2 = Move("Call Manager", 15, 5)
    move3 = Move("Scratch", 10, 10)
    test_pokemon1 = NormalPokemon("05", "Typicus", 10, move1, move2, move3)

    move4 = Move("Thunder", 2, 10)
    move5 = Move("Lighting", 10, 10)
    move6 = Move("Lightbulb", 12, 15)
    test_pokemon2 = ElectricPokemon("06", "Sparky", 50, move4, move5, move6)

    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)

    first_pokeball = test_trainer.trainer_belt[0]
    second_pokeball = test_trainer.trainer_belt[1]

    assert first_pokeball.pokemon == test_pokemon1
    assert second_pokeball.pokemon == test_pokemon2


def test_throw_pokeball_catch_pokemon_while_some_pokemon_caught_already():
    """
    Test that a trainer can continue catching Pokemon even after having
        caught previous Pokemon, ensuring the Pokemon are placed in successive
            Pokeballs in the trainer's belt.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Complain", 5, 10)
    move2 = Move("Call Manager", 15, 5)
    move3 = Move("Scratch", 10, 10)
    test_pokemon1 = NormalPokemon("05", "Typicus", 10, move1, move2, move3)

    test_trainer.throw_pokeball(test_pokemon1)

    first_pokeball = test_trainer.trainer_belt[0]
    assert first_pokeball.pokemon == test_pokemon1

    move4 = Move("Thunder", 2, 10)
    move5 = Move("Lighting", 10, 10)
    move6 = Move("Lightbulb", 12, 15)
    test_pokemon2 = ElectricPokemon("06", "Sparky", 50, move4, move5, move6)

    test_trainer.throw_pokeball(test_pokemon2)

    second_pokeball = test_trainer.trainer_belt[1]
    assert second_pokeball.pokemon == test_pokemon2


def test_throw_pokeball_does_not_catch_pokemon_if_no_available_pokeballs():
    """
    Test that a trainer cannot catch a Pokemon if there are no available
        Pokeballs left in the belt. It should raise a NoEmptyPokeballError.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon1 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon2 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon3 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    move10 = Move("Complain", 5, 10)
    move11 = Move("Call Manager", 15, 5)
    move12 = Move("Scratch", 10, 10)
    test_pokemon4 = NormalPokemon("05", "Typicus", 10, move10, move11, move12)

    move13 = Move("Thunder", 2, 10)
    move14 = Move("Lighting", 10, 10)
    move15 = Move("Lightbulb", 12, 15)
    test_pokemon5 = ElectricPokemon("06", "Sparky", 50, move13, move14, move15)

    move16 = Move("Light Punch", 10, 15)
    move17 = Move("Light Kick", 15, 10)
    move18 = Move("Fatal Punch", 20, 5)
    test_pokemon6 = FightingPokemon(
        "07", "One-Puncher", 75, move16, move17, move18
    )

    move19 = Move("Irregular", 15, 12)
    move20 = Move("Sting", 12, 20)
    move21 = Move("Sleep", 8, 35)
    test_pokemon7 = PoisonPokemon("08", "Foxglove", 45, move19, move20, move21)

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


def test_trainer_belt_space_returns_true_when_all_space():
    """
    Test that the belt_space method returns True when there is space available
        on the trainer's belt for more Pokemon.
    """
    test_trainer = Trainer("Scrooge")

    assert test_trainer.belt_space() is True


def test_trainer_belt_space_returns_true_when_some_space():
    """
    Test that the belt_space method returns True when there is some space
        available on the trainer's belt after catching a few Pokemon.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Complain", 5, 10)
    move2 = Move("Call Manager", 15, 5)
    move3 = Move("Scratch", 10, 10)
    test_pokemon1 = NormalPokemon("05", "Typicus", 10, move1, move2, move3)

    move4 = Move("Thunder", 2, 10)
    move5 = Move("Lighting", 10, 10)
    move6 = Move("Lightbulb", 12, 15)
    test_pokemon2 = ElectricPokemon("06", "Sparky", 50, move4, move5, move6)

    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)

    assert test_trainer.belt_space() is True


def test_trainer_belt_space_returns_false_when_no_space():
    """
    Test that the belt_space method returns False when there is no space
        available on the trainer's belt to catch more Pokemon.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon1 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon2 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon3 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    move10 = Move("Complain", 5, 10)
    move11 = Move("Call Manager", 15, 5)
    move12 = Move("Scratch", 10, 10)
    test_pokemon4 = NormalPokemon("05", "Typicus", 10, move10, move11, move12)

    move13 = Move("Thunder", 2, 10)
    move14 = Move("Lighting", 10, 10)
    move15 = Move("Lightbulb", 12, 15)
    test_pokemon5 = ElectricPokemon("06", "Sparky", 50, move13, move14, move15)

    move16 = Move("Light Punch", 10, 15)
    move17 = Move("Light Kick", 15, 10)
    move18 = Move("Fatal Punch", 20, 5)
    test_pokemon6 = FightingPokemon(
        "07", "One-Puncher", 75, move16, move17, move18
    )

    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    test_trainer.throw_pokeball(test_pokemon3)
    test_trainer.throw_pokeball(test_pokemon4)
    test_trainer.throw_pokeball(test_pokemon5)
    test_trainer.throw_pokeball(test_pokemon6)

    assert test_trainer.belt_space() is False


def test_trainer_get_pokemon_by_id_if_pokemon_available():
    """
    Test that the get_pokemon_by_id method correctly retrieves a Pokemon
        by its ID, and that the string representation of the Pokemon matches
            the expected format.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon1 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon2 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon3 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    test_trainer.throw_pokeball(test_pokemon3)

    assert test_trainer.get_pokemon_by_id("02").name == "Infernus"
    assert test_trainer.get_pokemon_by_id("04").name == "Voda"
    assert test_trainer.get_pokemon_by_id("03").name == "Herbus"

    expected_output = (
        "04: Voda, Water type, HP: 60\n"
        "Move: Hurricane, AP: 10, PP: 5\n"
        "Move: Surf, AP: 15, PP: 10\n"
        "Move: Cowabunga, AP: 20, PP: 5\n"
    )
    assert str(test_trainer.get_pokemon_by_id("04")) == expected_output


def test_trainer_get_pokemon_by_id_if_no_pokemon_available():
    """
    Test that the get_pokemon_by_id method returns None when no Pokemon
        with the specified ID is found on the trainer's belt.
    """
    test_trainer = Trainer("Scrooge")

    assert test_trainer.get_pokemon_by_id("04") is None


def test_trainer_str_method_return_expected_output_when_all_empty_pkbls():
    """
    Test that the __str__ method correctly returns the expected string output
        when the trainer's belt is empty (no Pokemon caught yet).
    """
    test_trainer = Trainer("Scrooge")
    expected_output = (
        "You have 0 pokemon's with you,\n" "you can catch 6 more."
    )
    assert str(test_trainer) == expected_output


def test_trainer_str_method_return_expected_output_when_all_some_pokeballs():
    """
    Test that the __str__ method correctly returns the expected string output
        when the trainer has some Pokemon caught in the Pokeballs.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon1 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon2 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon3 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    test_trainer.throw_pokeball(test_pokemon3)
    expected_output = (
        "You have 3 pokemon's with you,\n" "you can catch 3 more."
    )
    assert str(test_trainer) == expected_output


def test_trainer_str_method_return_expected_output_when_all_none_pokeballs():
    """
    Test that the __str__ method correctly returns the expected string output
        when the trainer's belt is full, with 6 Pokemon caught.
    """
    test_trainer = Trainer("Scrooge")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon1 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon2 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon3 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    move10 = Move("Complain", 5, 10)
    move11 = Move("Call Manager", 15, 5)
    move12 = Move("Scratch", 10, 10)
    test_pokemon4 = NormalPokemon("05", "Typicus", 10, move10, move11, move12)

    move13 = Move("Thunder", 2, 10)
    move14 = Move("Lighting", 10, 10)
    move15 = Move("Lightbulb", 12, 15)
    test_pokemon5 = ElectricPokemon("06", "Sparky", 50, move13, move14, move15)

    move16 = Move("Light Punch", 10, 15)
    move17 = Move("Light Kick", 15, 10)
    move18 = Move("Fatal Punch", 20, 5)
    test_pokemon6 = FightingPokemon(
        "07", "One-Puncher", 75, move16, move17, move18
    )

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
