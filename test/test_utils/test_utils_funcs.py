from src.utils.utils_funcs import (
    input_manager,
    pokemon_data_reader,
    pokemon_table_display,
    create_pokemon_instance,
    catch_random_pokemon,
    get_pokemon_data,
    trainer_setup,
    select_starting_pokemon,
)
from rich.table import Table
from src.classes.pokemon import (
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
import pytest
import random
from src.classes.trainer import Trainer
from unittest.mock import patch


def test_input_manager_valid_input():
    """Test the get_non_empty_input function handles input as expected."""

    with patch("builtins.input", return_value="testing"):
        assert input_manager("") is not None
        assert input_manager("") == "testing"


def test_input_manager_invalid_followed_by_valid_input(capsys):
    """Test the get_non_empty_input function handles no input as expected."""

    with patch("builtins.input", side_effect=["", "testing"]):
        result = input_manager("")
        assert result == "testing"
        captured = capsys.readouterr()
        assert "Input cannot be empty, please try again." in captured.out


def test_pokemon_data_reader_returns_expected_format():
    result = pokemon_data_reader(location="test/test_pokemon_data.md")
    assert isinstance(result, list)
    for pokemon in result:
        assert isinstance(pokemon, dict)
    assert len(result) == 14


def test_pokemon_data_reader_returns_expected_values():
    result = pokemon_data_reader(location="test/test_pokemon_data.md")
    assert result[0] == {
        "Id": "01",
        "Name": "Typicus",
        "Type": "Normal",
        "Hitpoints": "10",
        "Move 01": "Complain",
        "Damage 01": "5",
        "Powerpoints 01": "10",
        "Move 02": "Call Manager",
        "Damage 02": "15",
        "Powerpoints 02": "5",
        "Move 03": "Scratch",
        "Damage 03": "10",
        "Powerpoints 03": "10",
        "Strength": "None",
        "Weakness": "Fighting",
        "Sound": "How very dare you!",
    }
    assert result[1] == {
        "Id": "02",
        "Name": "Grass Pokemon",
        "Type": "Grass",
        "Hitpoints": "1",
        "Move 01": "Test Move",
        "Damage 01": "1",
        "Powerpoints 01": "1",
        "Move 02": "Test Move",
        "Damage 02": "2",
        "Powerpoints 02": "2",
        "Move 03": "Test Move",
        "Damage 03": "3",
        "Powerpoints 03": "3",
        "Strength": "Water",
        "Weakness": "Fire",
        "Sound": "Test Sound",
    }
    assert result[2] == {
        "Id": "03",
        "Name": "Fire Pokemon",
        "Type": "Fire",
        "Hitpoints": "1",
        "Move 01": "Test Move",
        "Damage 01": "1",
        "Powerpoints 01": "1",
        "Move 02": "Test Move",
        "Damage 02": "2",
        "Powerpoints 02": "2",
        "Move 03": "Test Move",
        "Damage 03": "3",
        "Powerpoints 03": "3",
        "Strength": "Grass",
        "Weakness": "Water",
        "Sound": "Test Sound",
    }


def test_pokemon_table_display_returns_expected_format():
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    result = pokemon_table_display(test_data)
    assert isinstance(result, Table)
    assert len(result.columns) == 16
    assert result.row_count == 14


def test_pokemon_table_display_returns_expected_header_values():
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    result = pokemon_table_display(test_data)
    expected_headers = [
        "Id",
        "Name",
        "Type",
        "Hitpoints",
        "Move 01",
        "Damage 01",
        "Powerpoints 01",
        "Move 02",
        "Damage 02",
        "Powerpoints 02",
        "Move 03",
        "Damage 03",
        "Powerpoints 03",
        "Strength",
        "Weakness",
        "Sound",
    ]

    actual_headers = [col.header for col in result.columns]

    assert actual_headers == expected_headers


def test_create_pokemon_instance_values_as_expected():
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    pokemon_dict_01 = test_data[0]

    result_01 = create_pokemon_instance(pokemon_dict_01)

    assert isinstance(result_01, NormalPokemon)
    assert result_01.pokemon_id == "01"
    assert result_01.name == "Typicus"
    assert result_01.type == "Normal"
    assert result_01.hit_points == 10
    assert result_01.moves[0].name == "Complain"
    assert result_01.moves[0].damage == 5
    assert result_01.moves[0].powerpoints == 10
    assert result_01.moves[1].name == "Call Manager"
    assert result_01.moves[1].damage == 15
    assert result_01.moves[1].powerpoints == 5
    assert result_01.moves[2].name == "Scratch"
    assert result_01.moves[2].damage == 10
    assert result_01.moves[2].powerpoints == 10


def test_create_pokemon_instance_subclasses_as_expected():
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")

    pokemon_dict_02 = test_data[1]
    pokemon_dict_03 = test_data[2]
    pokemon_dict_04 = test_data[3]
    pokemon_dict_05 = test_data[4]
    pokemon_dict_06 = test_data[5]
    pokemon_dict_07 = test_data[6]
    pokemon_dict_08 = test_data[7]
    pokemon_dict_09 = test_data[8]
    pokemon_dict_10 = test_data[9]
    pokemon_dict_11 = test_data[10]
    pokemon_dict_12 = test_data[11]
    pokemon_dict_13 = test_data[12]

    result_02 = create_pokemon_instance(pokemon_dict_02)
    result_03 = create_pokemon_instance(pokemon_dict_03)
    result_04 = create_pokemon_instance(pokemon_dict_04)
    result_05 = create_pokemon_instance(pokemon_dict_05)
    result_06 = create_pokemon_instance(pokemon_dict_06)
    result_07 = create_pokemon_instance(pokemon_dict_07)
    result_08 = create_pokemon_instance(pokemon_dict_08)
    result_09 = create_pokemon_instance(pokemon_dict_09)
    result_10 = create_pokemon_instance(pokemon_dict_10)
    result_11 = create_pokemon_instance(pokemon_dict_11)
    result_12 = create_pokemon_instance(pokemon_dict_12)
    result_13 = create_pokemon_instance(pokemon_dict_13)

    assert isinstance(result_02, GrassPokemon)
    assert isinstance(result_03, FirePokemon)
    assert isinstance(result_04, WaterPokemon)
    assert isinstance(result_05, ElectricPokemon)
    assert isinstance(result_06, FightingPokemon)
    assert isinstance(result_07, PoisonPokemon)
    assert isinstance(result_08, PsychicPokemon)
    assert isinstance(result_09, BugPokemon)
    assert isinstance(result_10, GhostPokemon)
    assert isinstance(result_11, DragonPokemon)
    assert isinstance(result_12, FairyPokemon)
    assert isinstance(result_13, GroundPokemon)


def test_create_pokemon_instance_raises_exception_as_expected():
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    pokemon_dict_14 = test_data[13]

    with pytest.raises(ValueError, match="Unknown Pokémon type: Ice"):
        create_pokemon_instance(pokemon_dict_14)


def test_catch_random_pokemon_returns_first_pokemon(monkeypatch):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    monkeypatch.setattr(random, "choice", lambda x: test_data[0])

    random_pokemon = catch_random_pokemon(location="test/test_pokemon_data.md")

    assert isinstance(random_pokemon, NormalPokemon)
    assert random_pokemon.pokemon_id == "01"
    assert random_pokemon.name == "Typicus"
    assert random_pokemon.type == "Normal"
    assert random_pokemon.hit_points == 10
    assert random_pokemon.moves[0].name == "Complain"
    assert random_pokemon.moves[0].damage == 5
    assert random_pokemon.moves[0].powerpoints == 10
    assert random_pokemon.moves[1].name == "Call Manager"
    assert random_pokemon.moves[1].damage == 15
    assert random_pokemon.moves[1].powerpoints == 5
    assert random_pokemon.moves[2].name == "Scratch"
    assert random_pokemon.moves[2].damage == 10
    assert random_pokemon.moves[2].powerpoints == 10


def test_catch_random_pokemon_returns_final_pokemon(monkeypatch):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    monkeypatch.setattr(random, "choice", lambda x: test_data[12])

    random_pokemon = catch_random_pokemon(location="test/test_pokemon_data.md")

    assert isinstance(random_pokemon, GroundPokemon)
    assert random_pokemon.pokemon_id == "13"
    assert random_pokemon.name == "Ground Pokemon"
    assert random_pokemon.type == "Ground"
    assert random_pokemon.hit_points == 1
    assert random_pokemon.moves[0].name == "Test Move"
    assert random_pokemon.moves[0].damage == 1
    assert random_pokemon.moves[0].powerpoints == 1
    assert random_pokemon.moves[1].name == "Test Move"
    assert random_pokemon.moves[1].damage == 2
    assert random_pokemon.moves[1].powerpoints == 2
    assert random_pokemon.moves[2].name == "Test Move"
    assert random_pokemon.moves[2].damage == 3
    assert random_pokemon.moves[2].powerpoints == 3


def test_get_pokemon_data_returns_expected_values_with_valid_id():
    expected_pokemon = get_pokemon_data(
        id_num=10, location="test/test_pokemon_data.md"
    )

    assert isinstance(expected_pokemon, GhostPokemon)
    assert expected_pokemon.pokemon_id == "10"
    assert expected_pokemon.name == "Ghost Pokemon"
    assert expected_pokemon.type == "Ghost"
    assert expected_pokemon.hit_points == 1
    assert expected_pokemon.moves[0].name == "Test Move"
    assert expected_pokemon.moves[0].damage == 1
    assert expected_pokemon.moves[0].powerpoints == 1
    assert expected_pokemon.moves[1].name == "Test Move"
    assert expected_pokemon.moves[1].damage == 2
    assert expected_pokemon.moves[1].powerpoints == 2
    assert expected_pokemon.moves[2].name == "Test Move"
    assert expected_pokemon.moves[2].damage == 3
    assert expected_pokemon.moves[2].powerpoints == 3


def test_get_pokemon_data_returns_expected_values_with_invalid_id():
    assert (
        get_pokemon_data(id_num=25, location="test/test_pokemon_data.md")
        is None
    )


@patch("builtins.input", side_effect=["Steve", "s", "10", "n"])
def test_trainer_setup_returns_instance_of_trainer_with_selected_one_pokemon(
    mock_input,
):
    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )
    assert test_trainer.space_on_belt == 5
    assert test_trainer.pokeball_01.pokemon.name == "Ghost Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch("builtins.input", side_effect=["Steve", "r", "n"])
def test_trainer_setup_returns_instance_of_trainer_with_random_one_pokemon(
    mock_input, monkeypatch
):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    monkeypatch.setattr(random, "choice", lambda x: test_data[0])

    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )
    assert test_trainer.space_on_belt == 5
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
    assert isinstance(test_trainer, Trainer) is True


@patch(
    "builtins.input",
    side_effect=["Steve", "s", "01", "y", "s", "02", "y", "s", "03", "n"],
)
def test_trainer_setup_returns_instance_of_trainer_with_selected_some_pokemon(
    mock_input,
):
    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )
    assert test_trainer.space_on_belt == 3
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
    assert test_trainer.pokeball_02.pokemon.name == "Grass Pokemon"
    assert test_trainer.pokeball_03.pokemon.name == "Fire Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch(
    "builtins.input",
    side_effect=[
        "Steve",
        "s",
        "01",
        "y",
        "s",
        "02",
        "y",
        "s",
        "03",
        "y",
        "s",
        "04",
        "y",
        "s",
        "05",
        "y",
        "s",
        "06",
    ],
)
def test_trainer_setup_returns_instance_of_trainer_with_selected_max_pokemon(
    mock_input,
):
    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    assert test_trainer.space_on_belt == 0
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
    assert test_trainer.pokeball_02.pokemon.name == "Grass Pokemon"
    assert test_trainer.pokeball_03.pokemon.name == "Fire Pokemon"
    assert test_trainer.pokeball_04.pokemon.name == "Water Pokemon"
    assert test_trainer.pokeball_05.pokemon.name == "Electric Pokemon"
    assert test_trainer.pokeball_06.pokemon.name == "Fighting Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch("builtins.input", side_effect=["Steve", "r", "y", "r", "y", "r", "n"])
def test_trainer_setup_returns_instance_of_trainer_with_random_some_pokemon(
    mock_input, monkeypatch
):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")

    choices = [test_data[0], test_data[5], test_data[10]]

    def mock_random_choice(seq):
        return choices.pop(0)

    monkeypatch.setattr(random, "choice", mock_random_choice)

    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    assert test_trainer.space_on_belt == 3
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
    assert test_trainer.pokeball_02.pokemon.name == "Fighting Pokemon"
    assert test_trainer.pokeball_03.pokemon.name == "Dragon Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch(
    "builtins.input",
    side_effect=[
        "Steve",
        "r",
        "y",
        "r",
        "y",
        "r",
        "y",
        "r",
        "y",
        "r",
        "y",
        "r",
    ],
)
def test_trainer_setup_returns_instance_of_trainer_with_random_max_pokemon(
    mock_input, monkeypatch
):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")

    choices = [
        test_data[0],
        test_data[5],
        test_data[10],
        test_data[1],
        test_data[6],
        test_data[11],
    ]

    def mock_random_choice(seq):
        return choices.pop(0)

    monkeypatch.setattr(random, "choice", mock_random_choice)

    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    assert test_trainer.space_on_belt == 0
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
    assert test_trainer.pokeball_02.pokemon.name == "Fighting Pokemon"
    assert test_trainer.pokeball_03.pokemon.name == "Dragon Pokemon"
    assert test_trainer.pokeball_04.pokemon.name == "Grass Pokemon"
    assert test_trainer.pokeball_05.pokemon.name == "Poison Pokemon"
    assert test_trainer.pokeball_06.pokemon.name == "Fairy Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch(
    "builtins.input",
    side_effect=["Steve", "r", "y", "s", "05", "y", "r", "n"],
)
def test_trainer_setup_returns_instance_of_trainer_with_mixed_some_pokemon(
    mock_input, monkeypatch
):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")

    choices = [test_data[0], test_data[10]]

    def mock_random_choice(seq):
        return choices.pop(0)

    monkeypatch.setattr(random, "choice", mock_random_choice)

    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    assert test_trainer.space_on_belt == 3
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
    assert test_trainer.pokeball_02.pokemon.name == "Electric Pokemon"
    assert test_trainer.pokeball_03.pokemon.name == "Dragon Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch(
    "builtins.input",
    side_effect=[
        "Steve",
        "s",
        "12",
        "y",
        "s",
        "11",
        "y",
        "r",
        "y",
        "r",
        "y",
        "s",
        "01",
        "y",
        "r",
    ],
)
def test_trainer_setup_returns_instance_of_trainer_with_mixed_max_pokemon(
    mock_input, monkeypatch
):
    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")

    choices = [
        test_data[0],
        test_data[5],
        test_data[10],
    ]

    def mock_random_choice(seq):
        return choices.pop(0)

    monkeypatch.setattr(random, "choice", mock_random_choice)

    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    assert test_trainer.space_on_belt == 0
    assert test_trainer.pokeball_01.pokemon.name == "Fairy Pokemon"
    assert test_trainer.pokeball_02.pokemon.name == "Dragon Pokemon"
    assert test_trainer.pokeball_03.pokemon.name == "Typicus"
    assert test_trainer.pokeball_04.pokemon.name == "Fighting Pokemon"
    assert test_trainer.pokeball_05.pokemon.name == "Typicus"
    assert test_trainer.pokeball_06.pokemon.name == "Dragon Pokemon"
    assert isinstance(test_trainer, Trainer) is True


@patch("builtins.input", side_effect=["Steve", "s", "10", "n"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_if_selecting_pokemon(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_print.assert_any_call("Thank you for your choice.\n\n")


@patch("builtins.input", side_effect=["Steve", "r", "n"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_if_random_pokemon(
    mock_print, mock_input, monkeypatch
):

    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    monkeypatch.setattr(random, "choice", lambda x: test_data[0])

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )

    mock_print.assert_any_call("You caught a wild Typicus!")
    mock_print.assert_any_call("Thank you for your choice.\n\n")


@patch("builtins.input", side_effect=["Steve", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_if_pokemon_selection_cancelled(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )

    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "m", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_if_invalid_char_and_cancel(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call(
        "Invalid input. Please specify: "
        "[s]elect pokemon, choose [r]andom pokemon or [c]ancel.\n"
    )

    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "s", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_if_selecting_cancelled(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "s", "1000", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_if_selecting_with_invalid_id(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_print.assert_any_call("Pokemon not found, please try again.")
    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "s", "10", "m", "n"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_selecting_followed_by_inv_char(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )
    mock_input.assert_any_call(
        "Invalid input. Please specify: "
        "[y] to catch more pokemon or [n] to start the battle.\n"
    )

    mock_print.assert_any_call("Thank you for your choice.\n\n")


@patch("builtins.input", side_effect=["Steve", "s", "10", "y", "r", "n"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_selecting_followed_by_random(
    mock_print, mock_input, monkeypatch
):

    test_data = pokemon_data_reader(location="test/test_pokemon_data.md")
    monkeypatch.setattr(random, "choice", lambda x: test_data[0])

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )

    mock_print.assert_any_call("You caught a wild Typicus!")
    mock_print.assert_any_call("Thank you for your choice.\n\n")


@patch("builtins.input", side_effect=["Steve", "s", "10", "y", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_further_selecting_cancel(
    mock_print, mock_input
):
    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )

    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "s", "10", "y", "s", "01", "n"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_selecting_further_pokemon(
    mock_print, mock_input
):
    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_print.assert_any_call("Thank you for your choice.\n\n")


@patch("builtins.input", side_effect=["Steve", "s", "10", "y", "m", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_selecting_further_inv_char(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )

    mock_input.assert_any_call(
        "Invalid input. Please specify: "
        "[s]elect pokemon, choose [r]andom pokemon or [c]ancel.\n"
    )

    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch(
    "builtins.input", side_effect=["Steve", "s", "10", "y", "s", "1000", "c"]
)
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_selecting_further_inv_id(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )

    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect pokemon, "
        "choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_print.assert_any_call("Pokemon not found, please try again.")
    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "s", "10", "y", "s", "c"])
@patch("builtins.print")
def test_trainer_setup_returns_expected_output_selecting_followed_by_cancel(
    mock_print, mock_input
):

    trainer_setup(role="Test Trainer", location="test/test_pokemon_data.md")

    mock_input.assert_any_call("What's the Test Trainer's trainer name?\n")
    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect your first pokemon,"
        " choose [r]andom pokemon or [c]ancel?\n"
    )
    mock_input.assert_any_call("What's the pokemon id? (or [c]ancel)\n")

    mock_input.assert_any_call(
        "Test trainer, do you want to catch more pokemon? [y/n]\n"
    )

    mock_input.assert_any_call(
        "Test trainer, do you want to [s]elect pokemon, "
        "choose [r]andom pokemon or [c]ancel?\n"
    )

    mock_print.assert_any_call("Cancelled Pokemon selection.")


@patch("builtins.input", side_effect=["Steve", "c"])
@patch("builtins.print")
def test_select_starting_pokemon_with_no_pokemon(mock_print, mock_input):
    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    assert select_starting_pokemon(test_trainer) is None
    mock_print.assert_any_call(
        "\nSteve has chosen no Pokemon, ending the game."
    )


@patch("builtins.input", side_effect=["Steve", "s", "01", "n", "01"])
@patch("builtins.print")
def test_select_starting_pokemon_with_pokemon_and_valid_id(
    mock_print, mock_input
):
    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )
    test_pokemon = select_starting_pokemon(test_trainer)

    mock_input.assert_any_call("Steve, which Pokémon do you send out first?")

    mock_print.assert_any_call("\nSteve's available Pokémon:")
    mock_print.assert_any_call("01: Typicus, Type: Normal, HP: 10\n")

    assert isinstance(test_pokemon, NormalPokemon) is True
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"


@patch("builtins.input", side_effect=["Steve", "s", "01", "n", "1000", "01"])
@patch("builtins.print")
def test_select_starting_pokemon_with_pokemon_and_invalid_id(
    mock_print, mock_input
):
    test_trainer = trainer_setup(
        role="Test Trainer", location="test/test_pokemon_data.md"
    )

    test_pokemon = select_starting_pokemon(test_trainer)

    mock_input.assert_any_call("Steve, which Pokémon do you send out first?")

    mock_print.assert_any_call("\nSteve's available Pokémon:")
    mock_print.assert_any_call("01: Typicus, Type: Normal, HP: 10\n")
    mock_print.assert_any_call("Invalid Pokémon ID. Please try again.")

    assert isinstance(test_pokemon, NormalPokemon) is True
    assert test_trainer.pokeball_01.pokemon.name == "Typicus"
