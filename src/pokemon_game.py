from utils_funcs import input_manager, pokemon_data_reader
from battle import Battle


def pokemon_game():
    print(
        """
    ~~~~~~~~~~~~~~~~~~~~~~~~
          Welcome to
    Pokemon Battle Simulator
    ~~~~~~~~~~~~~~~~~~~~~~~~

    """
    )
    main_script()


def main_script():
    response = input_manager(
        "Please specify:\n"
        "[l]ist available pokemon, [p]lay a match or [e]xit the game."
    )
    while response.lower() not in "lpe":
        response = input_manager(
            "Invalid input. Please specify:\n"
            "[l]ist available pokemon, [p]lay a match or [e]xit the game."
        )

    if response.lower() == "e":
        print("Thank you for playing. Come battle again soon.")
        return

    if response.lower() == "l":
        pokemon_data_reader()
        main_script()

    if response.lower() == "p":
        trainer_01 = input_manager("What's the challenger's trainer name?")
        pokemon_01 = input_manager("What's the challenger's pokemon id?")
        trainer_02 = input_manager("What's the defender's trainer name?")
        pokemon_02 = input_manager("What's the defender's pokemon id?")
        battle = Battle(pokemon_01, pokemon_02)
        battle.get_winner()
        print(
            "Congratulations to the winner and their pokemon!\n"
            f"Thank you {trainer_01} and {trainer_02} for playing!"
        )
        response = input_manager(
            "Please specify:\n"
            "[p]lay again, [l]ist available pokemon, [e]xit the game."
        )
        while response.lower() not in "lpe":
            response = input_manager(
                "Invalid input. Please specify:\n"
                "[p]lay again, [l]ist available pokemon, [e]xit the game."
            )


if __name__ == "__main__":
    pokemon_game()
