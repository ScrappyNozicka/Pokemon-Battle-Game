from src.classes.battle import Battle, NoPokemonError
from src.classes.move import Move
from src.classes.trainer import Trainer
from src.classes.pokemon import FirePokemon
from src.classes.pokemon import WaterPokemon
from src.classes.pokemon import GrassPokemon
import pytest
from unittest.mock import patch, MagicMock


def test_battle_returns_trainer_values():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    assert test_battle.trainer_1.name == "Steve"
    assert isinstance(test_battle.trainer_1, Trainer)
    assert test_battle.trainer_2.name == "Paul"
    assert isinstance(test_battle.trainer_2, Trainer)


def test_battle_returns_pokemon_values():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    assert test_battle.pokemon_1.name == "Infernus"
    assert isinstance(test_battle.pokemon_1, FirePokemon)
    assert test_battle.pokemon_2.name == "Voda"
    assert isinstance(test_battle.pokemon_2, WaterPokemon)
    assert isinstance(test_battle.available_pokemon, list)
    assert test_battle.available_pokemon == [test_pokemon_01, test_pokemon_02]


def test_battle_returns_pokemon_turn_value():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    assert test_battle.pokemon_1_turn is not None
    assert test_battle.pokemon_1_turn is True


def test_battle_change_available_pokemon_challenger_trainer():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_01.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )
    test_battle._Battle__change_pokemon(pokemon_id_to_change="04")

    assert test_battle.pokemon_1.name == "Voda"
    assert isinstance(test_battle.pokemon_1, WaterPokemon)


def test_battle_change_available_pokemon_defender_trainer():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_02.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    test_battle.pokemon_1_turn = False
    test_battle._Battle__change_pokemon(pokemon_id_to_change="03")

    assert test_battle.pokemon_2.name == "Herbus"
    assert isinstance(test_battle.pokemon_2, GrassPokemon)


def test_battle_change_unavailable_pokemon_challenger_trainer():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_03
    )

    with pytest.raises(
        NoPokemonError, match="Pokemon ID is invalid or unavailable."
    ):
        test_battle._Battle__change_pokemon(pokemon_id_to_change="04")


@patch("builtins.input", side_effect=["04"])
@patch("builtins.print")
def test_battle_force_switch_challenger_available_pokemon(
    mock_print, mock_input
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_01.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_pokemon_01.hit_points = 0

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_03
    )

    switched_pokemon = test_battle._Battle__force_switch(test_trainer_01)

    assert switched_pokemon.name == "Voda"
    assert isinstance(switched_pokemon, WaterPokemon)

    mock_input.assert_any_call("Steve, choose a replacement Pokémon by ID:")

    mock_print.assert_any_call("Steve, your pokemon has fainted!")
    mock_print.assert_any_call("Steve's available Pokémon:")
    mock_print.assert_any_call("04: Voda, Type: Water, HP: 60")
    mock_print.assert_any_call("Steve sent out Voda!")


@patch("builtins.input", side_effect=["03"])
@patch("builtins.print")
def test_battle_force_switch_defender_available_pokemon(
    mock_print, mock_input
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_02.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_pokemon_02.hit_points = 0

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    switched_pokemon = test_battle._Battle__force_switch(test_trainer_02)

    assert switched_pokemon.name == "Herbus"
    assert isinstance(switched_pokemon, GrassPokemon)

    mock_input.assert_any_call("Paul, choose a replacement Pokémon by ID:")

    mock_print.assert_any_call("Paul, your pokemon has fainted!")
    mock_print.assert_any_call("Paul's available Pokémon:")
    mock_print.assert_any_call("03: Herbus, Type: Grass, HP: 45")
    mock_print.assert_any_call("Paul sent out Herbus!")


@patch("builtins.input", side_effect=["04"])
@patch("builtins.print")
def test_battle_force_switch_challenger_no_available_pokemon(
    mock_print, mock_input
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_01.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_pokemon_01.hit_points = 0
    test_pokemon_02.hit_points = 0

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_03
    )

    switched_pokemon = test_battle._Battle__force_switch(test_trainer_01)

    assert switched_pokemon is None

    mock_print.assert_any_call("Steve, your pokemon has fainted!")
    mock_print.assert_any_call("Steve has no more usable pokemon!")


@patch("builtins.input", side_effect=["999", "04"])
@patch("builtins.print")
def test_battle_force_switch_challenger_invalid_id(mock_print, mock_input):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_01.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_pokemon_01.hit_points = 0

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_03
    )

    switched_pokemon = test_battle._Battle__force_switch(test_trainer_01)

    assert switched_pokemon.name == "Voda"
    assert isinstance(switched_pokemon, WaterPokemon)

    mock_input.assert_any_call("Steve, choose a replacement Pokémon by ID:")

    mock_print.assert_any_call("Steve, your pokemon has fainted!")
    mock_print.assert_any_call("Steve's available Pokémon:")
    mock_print.assert_any_call("04: Voda, Type: Water, HP: 60")
    mock_print.assert_any_call(
        "Invalid choice or that Pokémon has fainted. Try again."
    )
    mock_print.assert_any_call("Steve sent out Voda!")


@patch("builtins.input", side_effect=["1"])
@patch("builtins.print")
def test_battle_select_move_valid_input(mock_print, mock_input):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )
    test_battle._Battle__pokemon_attack = MagicMock()

    selected_move = test_battle._Battle__select_move()

    mock_print.assert_any_call("Available moves:")
    mock_print.assert_any_call("1. Flamethrow (AP: 10, " "PP: 10/10)")
    mock_print.assert_any_call("2. Ember (AP: 15, " "PP: 3/3)")
    mock_print.assert_any_call("3. Lavalamp (AP: 20, " "PP: 2/2)")

    mock_input.assert_any_call("Select move by number:")

    assert selected_move == move1

    test_battle._Battle__pokemon_attack.assert_called_with(move1)


@patch("builtins.input", side_effect=["magic", "999", "03"])
@patch("builtins.print")
def test_battle_select_move_invalid_input(mock_print, mock_input):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )
    test_battle._Battle__pokemon_attack = MagicMock()

    selected_move = test_battle._Battle__select_move()

    mock_print.assert_any_call("Available moves:")
    mock_print.assert_any_call("1. Flamethrow (AP: 10, " "PP: 10/10)")
    mock_print.assert_any_call("2. Ember (AP: 15, " "PP: 3/3)")
    mock_print.assert_any_call("3. Lavalamp (AP: 20, " "PP: 2/2)")

    mock_print.assert_any_call("Please enter a number.")
    mock_print.assert_any_call("Invalid move number. Try again.")

    assert selected_move == move3

    test_battle._Battle__pokemon_attack.assert_called_with(move3)


@patch("builtins.input", side_effect=["s", "04"])
@patch("builtins.print")
def test_battle_select_action_valid_switch_action_input(
    mock_print, mock_input
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_01.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_03
    )

    test_battle._Battle__select_action()

    mock_input.assert_any_call(
        "Please select action: [s]witch pokemon "
        "or [a]ttack and select move.\n"
    )

    mock_print.assert_any_call("Steve switched to Voda.")


@patch("builtins.input", side_effect=["a", "1"])
@patch("builtins.print")
def test_battle_select_action_valid_attack_action_input(
    mock_print, mock_input
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    test_battle._Battle__pokemon_attack = MagicMock()

    test_battle._Battle__select_action()

    mock_input.assert_any_call(
        "Please select action: [s]witch pokemon "
        "or [a]ttack and select move.\n"
    )

    mock_print.assert_any_call("Available moves:")
    mock_print.assert_any_call("1. Flamethrow (AP: 10, " "PP: 10/10)")
    mock_print.assert_any_call("2. Ember (AP: 15, " "PP: 3/3)")
    mock_print.assert_any_call("3. Lavalamp (AP: 20, " "PP: 2/2)")

    mock_input.assert_any_call("Select move by number:")

    test_battle._Battle__pokemon_attack.assert_called_with(move1)


@patch("builtins.input", side_effect=["999", "s", "04"])
@patch("builtins.print")
def test_battle_select_action_invalid_input(mock_print, mock_input):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_01.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_03
    )

    test_battle._Battle__select_action()

    mock_input.assert_any_call(
        "Please select action: [s]witch pokemon "
        "or [a]ttack and select move.\n"
    )

    mock_print.assert_any_call("Invalid action. Please try again.")


def test_battle_get_damage_standard(monkeypatch):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    expected_damage = test_battle._Battle__get_damage(move1)

    assert isinstance(expected_damage, float)
    assert expected_damage == 5


def test_battle_get_damage_critical(monkeypatch):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 20)

    expected_damage = test_battle._Battle__get_damage(move1)

    assert isinstance(expected_damage, float)
    assert expected_damage == 7.5


@patch("builtins.print")
def test_battle_pokemon_attack_valid_powerpoints(mock_print, monkeypatch):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    test_battle._Battle__pokemon_attack(move1)

    mock_print.assert_any_call("Infernus used Flamethrow (AP: 10)")
    mock_print.assert_any_call(
        "Voda has taken 5.0 damage and has 55.0 HP left."
    )


@patch("builtins.print")
def test_battle_pokemon_attack_invalid_powerpoints(mock_print, monkeypatch):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 0)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 60, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    test_attack = test_battle._Battle__pokemon_attack(move1)

    mock_print.assert_any_call(
        "Infernus can't use Flamethrow! " "Not enough PowerPoints."
    )
    assert test_attack is None


@patch("builtins.input", side_effect=["03"])
@patch("builtins.print")
def test_battle_pokemon_attack_defender_pokemon_fainted(
    mock_print, mock_input, monkeypatch
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 5, move4, move5, move6)

    move7 = Move("Grow", 10, 10)
    move8 = Move("Bloom", 13, 8)
    move9 = Move("Thorn Whip", 16, 6)
    test_pokemon_03 = GrassPokemon("03", "Herbus", 45, move7, move8, move9)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_02.throw_pokeball(test_pokemon_02)
    test_trainer_02.throw_pokeball(test_pokemon_03)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    test_battle._Battle__pokemon_attack(move1)

    mock_print.assert_any_call("Infernus used Flamethrow (AP: 10)")
    mock_print.assert_any_call(
        "Voda has taken 5.0 damage and has 0.0 HP left."
    )
    mock_print.assert_any_call("Paul switched to Herbus!")


@patch("builtins.print")
def test_battle_pokemon_attack_defender_no_pokemon_left(
    mock_print, monkeypatch
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 5, move4, move5, move6)

    test_trainer_01.throw_pokeball(test_pokemon_01)
    test_trainer_02.throw_pokeball(test_pokemon_02)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    test_battle._Battle__pokemon_attack(move1)

    mock_print.assert_any_call("Infernus used Flamethrow (AP: 10)")
    mock_print.assert_any_call(
        "Voda has taken 5.0 damage and has 0.0 HP left."
    )
    mock_print.assert_any_call("Paul has no Pokémon left!")


@patch("builtins.input", side_effect=["a", "1"])
@patch("builtins.print")
def test_battle_take_turn_challenger_win_defender_faints(
    mock_print, mock_input, monkeypatch
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 30, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 5, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    test_battle.take_turn()

    assert test_pokemon_02.hit_points == 0.0

    mock_print.assert_any_call("\nIt's Infernus's turn!")
    mock_print.assert_any_call("Voda has fainted!")


@patch("builtins.input", side_effect=["a", "1", "a", "1"])
@patch("builtins.print")
def test_battle_take_turn_defender_win_challenger_faints(
    mock_print, mock_input, monkeypatch
):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 15, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 10, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    test_battle.take_turn()

    assert test_pokemon_01.hit_points == 0.0
    assert test_pokemon_02.hit_points == 5.0

    mock_print.assert_any_call("\nIt's Infernus's turn!")
    mock_print.assert_any_call(
        "Voda has taken 5.0 damage and has 5.0 HP left."
    )
    mock_print.assert_any_call("\nIt's Voda's turn!")
    mock_print.assert_any_call(
        "Infernus has taken 15.0 damage and has 0.0 HP left."
    )
    mock_print.assert_any_call("Infernus has fainted!")


@patch("builtins.input", side_effect=["a", "1", "a", "1"])
@patch("builtins.print")
def test_battle_get_winner_challenger_pokemon_faints(mock_print, mock_input):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 15, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 10, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    test_battle.take_turn()

    test_winner = test_battle._Battle__get_winner()

    assert isinstance(test_winner, bool)
    assert test_winner is True

    mock_print.assert_any_call("Infernus has fainted!")


@patch("builtins.input", side_effect=["a", "1"])
@patch("builtins.print")
def test_battle_get_winner_defender_pokemon_faints(mock_print, mock_input):
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 60, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 5, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    test_battle.take_turn()

    test_winner = test_battle._Battle__get_winner()

    assert isinstance(test_winner, bool)
    assert test_winner is True

    mock_print.assert_any_call("Voda has fainted!")


def test_battle_get_winner_none_fainted():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 60, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 45, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    test_winner = test_battle._Battle__get_winner()

    assert isinstance(test_winner, bool)
    assert test_winner is False


def test_battle_str_method_returns_expected_output_when_challenger_turn():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 60, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 45, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    expected_output = (
        "Battle between:\n" "Infernus\n" "Voda\n" "Next turn: Infernus"
    )

    assert str(test_battle) == expected_output


def test_battle_str_method_returns_expected_output_when_defender_turn():
    test_trainer_01 = Trainer(trainer_name="Steve")
    test_trainer_02 = Trainer(trainer_name="Paul")

    move1 = Move("Flamethrow", 10, 10)
    move2 = Move("Ember", 15, 3)
    move3 = Move("Lavalamp", 20, 2)
    test_pokemon_01 = FirePokemon("02", "Infernus", 60, move1, move2, move3)

    move4 = Move("Hurricane", 10, 5)
    move5 = Move("Surf", 15, 10)
    move6 = Move("Cowabunga", 20, 5)
    test_pokemon_02 = WaterPokemon("04", "Voda", 45, move4, move5, move6)

    test_battle = Battle(
        test_trainer_01, test_trainer_02, test_pokemon_01, test_pokemon_02
    )

    test_battle.pokemon_1_turn = False

    expected_output = (
        "Battle between:\n" "Infernus\n" "Voda\n" "Next turn: Voda"
    )

    assert str(test_battle) == expected_output
