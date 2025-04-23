from src.utils_funcs import input_manager

# pokemon_data_reader,
# pokemon_table_display,
# create_pokemon_instance,
# catch_random_pokemon,
# get_pokemon_data,
# trainer_setup,
# select_starting_pokemon
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
