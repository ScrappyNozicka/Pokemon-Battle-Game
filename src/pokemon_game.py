from src.utils_funcs import (
    input_manager,
    pokemon_data_reader,
    pokemon_table_display,
    trainer_setup,
    select_starting_pokemon,
)
from src.battle import Battle
from src.trainer import Trainer


def pokemon_game():
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
    choice = input_manager(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )
    while choice.lower() not in "lpe":
        choice = input_manager(
            "Invalid input. Please specify: "
            "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
        )

    if choice.lower() == "e":
        print("Thank you for playing. Come battle again soon.")
        return

    if choice.lower() == "l":
        data = pokemon_data_reader()
        pokemon_table_display(data)
        main_script()

    if choice.lower() == "p":
        trainer_01 = trainer_setup("challenger")
        trainer_02 = trainer_setup("defender")

        pokemon_01 = select_starting_pokemon(trainer_01)
        pokemon_02 = select_starting_pokemon(trainer_02)

        print(f"\n{trainer_01.name} has chosen:\n{pokemon_01}")
        print(f"\n{trainer_02.name} has chosen:\n{pokemon_02}\n")

        battle = Battle(trainer_01, trainer_02, pokemon_01, pokemon_02)

        winner = battle.take_turn()

        if winner == pokemon_01:
            print(
                f"Congratulations to {trainer_01.name} and {pokemon_01.name}."
            )
        else:
            print(
                f"Congratulations to {trainer_02.name} and {pokemon_02.name}."
            )
        main_script()


if __name__ == "__main__":
    pokemon_game()
