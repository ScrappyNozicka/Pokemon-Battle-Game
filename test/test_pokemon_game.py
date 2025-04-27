from src.pokemon_game import pokemon_game, main_script
from unittest.mock import patch


@patch("builtins.input", side_effect=["e"])
@patch("builtins.print")
def test_pokemon_game_return_welcome_message(mock_print, mock_input):
    """
    Test that the welcome message is printed when the game starts.
    """
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
    """
    Test that invalid menu input prompts the user again.
    """
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
    """
    Test that the game exits accordingly with a farewell message.
    """
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
    """
    Test listing available Pokemon using the 'list' menu option.
    """
    mock_reader.return_value = ["Infernus", "Typicus"]

    main_script()

    mock_reader.assert_called_once()
    mock_display.assert_called_once_with(["Infernus", "Typicus"])


@patch(
    "builtins.input",
    side_effect=[
        "p",
        "Steve",
        "s",
        "03",
        "n",
        "Paul",
        "s",
        "02",
        "n",
        "03",
        "02",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "e",
    ],
)
@patch("builtins.print")
def test_pokemon_game_main_script_challenger_wins_match(
    mock_print, mock_input, monkeypatch
):
    """
    Simulate a match where the challenger wins
        and verify the correct victory message.
    """
    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    main_script()

    mock_input.assert_any_call(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )

    mock_print.assert_any_call("\nSteve has chosen:")
    mock_print.assert_any_call("\nPaul has chosen:")
    mock_print.assert_any_call("Congratulations to Steve.")


@patch(
    "builtins.input",
    side_effect=[
        "p",
        "Steve",
        "s",
        "02",
        "n",
        "Paul",
        "s",
        "03",
        "n",
        "02",
        "03",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "a",
        "1",
        "e",
    ],
)
@patch("builtins.print")
def test_pokemon_game_main_script_defender_wins_match(
    mock_print, mock_input, monkeypatch
):
    """
    Simulate a match where the defender wins
        and verify the correct victory message.
    """
    monkeypatch.setattr("random.randint", lambda *args, **kwargs: 1)

    main_script()

    mock_input.assert_any_call(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )

    mock_print.assert_any_call("\nSteve has chosen:")
    mock_print.assert_any_call("\nPaul has chosen:")
    mock_print.assert_any_call("Congratulations to Paul.")


@patch(
    "builtins.input",
    side_effect=[
        "p",
        "Steve",
        "c",
        "Paul",
        "s",
        "03",
        "n",
        "e",
    ],
)
@patch("builtins.print")
def test_pokemon_game_main_script_challenger_selected_no_pokemon(
    mock_print, mock_input
):
    """
    Test scenario where the challenger chooses no Pokemon
        and returns to the main menu.
    """
    main_script()

    mock_input.assert_any_call(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )

    mock_print.assert_any_call(
        "\nSteve has chosen no Pokemon, returning to main menu."
    )


@patch(
    "builtins.input",
    side_effect=[
        "p",
        "Steve",
        "s",
        "03",
        "n",
        "Paul",
        "c",
        "e",
    ],
)
@patch("builtins.print")
def test_pokemon_game_main_script_defender_selected_no_pokemon(
    mock_print, mock_input
):
    """
    Test scenario where the defender chooses no Pokemon
        and returns to the main menu.
    """
    main_script()

    mock_input.assert_any_call(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )

    mock_print.assert_any_call(
        "\nPaul has chosen no Pokemon, returning to main menu."
    )
