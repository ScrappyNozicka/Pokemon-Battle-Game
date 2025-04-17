from utils_funcs import (
    input_manager,
    pokemon_data_reader,
    pokemon_table_display,
    get_pokemon_data,
)
from battle import Battle
from trainer import Trainer


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
    response = input_manager(
        "Please specify: "
        "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
    )
    while response.lower() not in "lpe":
        response = input_manager(
            "Invalid input. Please specify: "
            "[l]ist available pokemon, [p]lay a match or [e]xit the game.\n"
        )

    if response.lower() == "e":
        print("Thank you for playing. Come battle again soon.")
        return

    if response.lower() == "l":
        data = pokemon_data_reader()
        pokemon_table_display(data)
        main_script()

    if response.lower() == "p":
        trainer_01_name = input_manager(
            "What's the challenger's trainer name?\n"
        )
        trainer_01 = Trainer(trainer_01_name)
        print(trainer_01)
        while trainer_01.belt_space():
            pokemon_id = input_manager("What's the challenger's pokemon id?\n")
            pokemon = get_pokemon_data(pokemon_id)
            if not pokemon:
                print("Pokemon not found, please try again.")
            else:
                trainer_01.throw_pokeball(pokemon)

        trainer_02_name = input_manager(
            "What's the defender's trainer name?\n"
        )
        trainer_02 = Trainer(trainer_02_name)
        print(trainer_02)
        while trainer_02.belt_space():
            pokemon_id = input_manager("What's the defender's pokemon id?\n")
            pokemon = get_pokemon_data(pokemon_id)
            if not pokemon:
                print("Pokemon not found, please try again.")
            else:
                trainer_02.throw_pokeball(pokemon)

        pokemon_01_name = input_manager(
            f"{trainer_01.name} which pokemon do you send out first?\n"
        )
        pokemon_02_name = input_manager(
            f"{trainer_02.name} which pokemon do you send out first?\n"
        )

        pokemon_01 = trainer_01.get_pokemon_by_name(pokemon_01_name)
        if not pokemon_01:
            print(f"{pokemon_01} not found! Please try again.")
            pokemon_01_name = input_manager(
                f"{trainer_01.name} which pokemon do you send out first?\n"
            )

        pokemon_02 = trainer_02.get_pokemon_by_name(pokemon_02_name)
        if not pokemon_02:
            print(f"{pokemon_02} not found! Please try again.")
            pokemon_02_name = input_manager(
                f"{trainer_02.name} which pokemon do you send out first?\n"
            )

        print(f"\n{trainer_01.name} has chosen:\n{pokemon_01}")
        print(f"\n{trainer_02.name} has chosen:\n{pokemon_02}\n")

        battle = Battle(pokemon_01, pokemon_02)

        winner = battle.take_turn()

        if winner == pokemon_01:
            print(
                f"Congratulations to {trainer_01.name} and {pokemon_01.name}."
            )
        else:
            print(
                f"Congratulations to {trainer_02.name} and {pokemon_02.name}."
            )
        response = input_manager(
            "Please specify: "
            "[p]lay again, [l]ist available pokemon, [e]xit the game.\n"
        )
        while response.lower() not in "lpe":
            response = input_manager(
                "Invalid input. Please specify: "
                "[p]lay again, [l]ist available pokemon, [e]xit the game.\n"
            )


if __name__ == "__main__":
    pokemon_game()
