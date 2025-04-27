from src.pokemon_game import pokemon_game, main_script
from unittest.mock import patch


@patch("builtins.input", side_effect=["e"])
@patch("builtins.print")
def test_pokemon_game_return_welcome_message(mock_print, mock_input):
    pokemon_game()

    mock_print.assert_any_call(
        """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              Welcome to
                        Pokemon Battle Simulator
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """
    )


@patch("builtins.input", side_effect=["999", "e"])
def test_pokemon_game_main_script_invalid_input(mock_input):
    main_script()

    mock_input.assert_any_call(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )
    mock_input.assert_any_call(
        "Invalid input. Please specify: "
        "[l]ist available pokemon, [p]lay a match "
        "or [e]xit the game.\n"
    )


@patch("builtins.input", side_effect=["e"])
@patch("builtins.print")
def test_pokemon_game_main_script_exit_the_game(mock_print, mock_input):
    main_script()

    mock_print.assert_any_call(
        "Thank you for playing. Come battle again soon."
    )


@patch("src.pokemon_game.pokemon_table_display")
@patch("src.pokemon_game.pokemon_data_reader")
@patch("builtins.input", side_effect=["l", "e"])
def test_pokemon_game_main_script_listing_pokemon(
    mock_input, mock_reader, mock_display
):

    mock_reader.return_value = ["Infernus", "Typicus"]

    main_script()

    mock_reader.assert_called_once()
    mock_display.assert_called_once_with(["Infernus", "Typicus"])


# def test_pokemon_game_main_script_challenger_wins_match(
# mock_print, mock_input):
# def test_pokemon_game_main_script_defender_wins_match(
# mock_print, mock_input):

# def test_pokemon_game_main_script_challenger_selected_no_pokemon(
# mock_print, mock_input):
# def test_pokemon_game_main_script_defender_selected_no_pokemon(
# mock_print, mock_input):
