from src.utils_funcs import (
    input_manager,
    pokemon_data_reader,
    pokemon_table_display,
    create_pokemon_instance,
    catch_random_pokemon,
    get_pokemon_data,
)

# trainer_setup,
# select_starting_pokemon
from unittest.mock import patch
from rich.table import Table
from src.pokemon import (
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
