from src.utils.utils_funcs import (
    input_manager,
    pokemon_data_reader,
    pokemon_table_display,
    trainer_setup,
    select_starting_pokemon,
)
from src.classes.battle import Battle


def pokemon_game():
    """
    Entry point for the Pokemon Battle Simulator game.

    Prints a welcome message and starts the main game loop.
    """
    print(
        """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              Welcome to
                        Pokemon Battle Simulator
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """
    )
    main_script()


def main_script():
    """
    Main game loop for the Pokemon Battle Simulator.

    Allows the player to:
    - List all available Pokemon.
    - Start a new battle match between two trainers.
    - Exit the game.

    Handles player input, sets up trainers and Pokemon,
    and initiates a turn-based battle.
    """
    while True:
        location = "pokemon_data.md"
        choice = input_manager(
            "Please specify: "
            "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
        )
        while choice.lower() not in "lpe":
            choice = input_manager(
                "Invalid input. Please specify: "
                "[l]ist available pokemon, [p]lay a match "
                "or [e]xit the game.\n"
            )

        if choice.lower() == "e":
            print("Thank you for playing. Come battle again soon.")
            break

        if choice.lower() == "l":
            data = pokemon_data_reader(location)
            pokemon_table_display(data)

        if choice.lower() == "p":
            trainer_01 = trainer_setup("challenger", location)
            trainer_02 = trainer_setup("defender", location)

            if trainer_01.space_on_belt == 6:
                print(
                    f"\n{trainer_01.name} has chosen no Pokemon, "
                    "returning to main menu."
                )
                continue

            if trainer_02.space_on_belt == 6:
                print(
                    f"\n{trainer_02.name} has chosen no Pokemon, "
                    "returning to main menu."
                )
                continue

            pokemon_01 = select_starting_pokemon(trainer_01)
            pokemon_02 = select_starting_pokemon(trainer_02)

            print(f"\n{trainer_01.name} has chosen:")
            print(pokemon_01)
            print(f"\n{trainer_02.name} has chosen:")
            print(pokemon_02)

            battle = Battle(trainer_01, trainer_02, pokemon_01, pokemon_02)

            winner = battle.take_turn()

            if winner == trainer_01:
                print(f"Congratulations to {trainer_01.name}.")
            else:
                print(f"Congratulations to {trainer_02.name}.")


if __name__ == "__main__":
    pokemon_game()
