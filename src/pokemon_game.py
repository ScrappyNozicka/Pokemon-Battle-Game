from utils_funcs import (
    input_manager,
    pokemon_data_reader,
    pokemon_table_display,
    get_pokemon_data,
    catch_random_pokemon
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
        if trainer_01.space_on_belt == 6:
            pokemon_selection_01 = input_manager("Challenger, do you want to [s]elect your first pokemon or choose one at [r]andom?\n")
            while pokemon_selection_01.lower() not in "sr":
                pokemon_selection_01 = input_manager(
                    "Invalid input. Please specify: "
                    "[s]elect your pokemon or choose [r]andom pokemon.\n"
                )
            if pokemon_selection_01.lower() == "s":
                while True:
                    pokemon_id = input_manager("What's the pokemon id? (or type 'q' to cancel)\n\n")
                    if pokemon_id.lower() == 'q':
                        print("Cancelled Pokémon selection.")
                        break
                    pokemon = get_pokemon_data(pokemon_id)
                    if pokemon:
                        trainer_01.throw_pokeball(pokemon)
                        break
                    else:
                        print("Pokemon not found, please try again.")
            elif pokemon_selection_01.lower() == "r":
                random_pokemon = catch_random_pokemon()
                trainer_01.throw_pokeball(random_pokemon)


        while trainer_01.belt_space():
            further_selection_01 = input_manager("Challenger, do you want to catch further pokemon? [y/n]\n")
            while further_selection_01.lower() not in "yn":
                further_selection_01 = input_manager(
                    "Invalid input. Please specify: "
                    "[y] to catch further pokemon or [n] to start the battle.\n"
                )
            if further_selection_01.lower() == "y": 
                pokemon_selection_1 = input_manager("Challenger, do you want to [s]elect your pokemon or choose one at [r]andom?\n")
                if pokemon_selection_1.lower() == "s":
                    pokemon_id = input_manager("What's the pokemon id?\n")
                    pokemon = get_pokemon_data(pokemon_id)
                    if not pokemon:
                        print("Pokemon not found, please try again.")
                    else:
                        trainer_01.throw_pokeball(pokemon)
                if pokemon_selection_1.lower() == "r":
                    random_pokemon = catch_random_pokemon()
                    trainer_01.throw_pokeball(random_pokemon)
            if further_selection_01.lower() == "n":
                print("thank you for your choice.\n")
                break
                        

        trainer_02_name = input_manager(
            "What's the defender's trainer name?\n"
        )
        trainer_02 = Trainer(trainer_02_name)
        print(trainer_02)
        if trainer_02.space_on_belt == 6:
            pokemon_selection = input_manager("Challenger, do you want to [s]elect your first pokemon or choose one at [r]andom?\n")
            while response.lower() not in "sr":
                response = input_manager(
                    "Invalid input. Please specify: "
                    "[s]elect your pokemon or choose [r]andom pokemon.\n"
                )
            if response == "s":
                pokemon_id = input_manager("What's the pokemon id?\n")
                pokemon = get_pokemon_data(pokemon_id)
                if not pokemon:
                    print("Pokemon not found, please try again.")
                else:
                    trainer_02.throw_pokeball(pokemon)
            if response == "r":
                random_pokemon = catch_random_pokemon()
                trainer_02.throw_pokeball(random_pokemon)

        while trainer_02.belt_space():
            response = input_manager("Challenger, do you want to catch further pokemon? [y/n]\n")
            while response.lower() not in "yn":
                response = input_manager(
                    "Invalid input. Please specify: "
                    "[y] to catch further pokemon or [n] to start the battle.\n"
                )
            if response == "y": 
                response = input_manager("Challenger, do you want to [s]elect your pokemon or choose one at [r]andom?\n")
                if response == "s":
                    pokemon_id = input_manager("What's the pokemon id?\n")
                    pokemon = get_pokemon_data(pokemon_id)
                    if not pokemon:
                        print("Pokemon not found, please try again.")
                    else:
                        trainer_02.throw_pokeball(pokemon)
                if response == "r":
                    random_pokemon = catch_random_pokemon()
                    trainer_02.throw_pokeball(random_pokemon)
            if response == "n":
                print("thank you for your choice.\n")
                break













        pokemon_01_name = input_manager(
            f"{trainer_01.name} which pokemon do you send out first?\n"
        )
        pokemon_02_name = input_manager(
            f"{trainer_02.name} which pokemon do you send out first?\n"
        )

        pokemon_01 = trainer_01.get_pokemon_by_name(pokemon_01_name)
        while not pokemon_01:
            pokemon_01_name = input_manager(
                f"{pokemon_01} not found! Please try again."
                f"{trainer_01.name} which pokemon do you send out first?\n"
        )

        pokemon_02 = trainer_02.get_pokemon_by_name(pokemon_02_name)
        while not pokemon_02:
            pokemon_02_name = input_manager(
                f"{pokemon_02} not found! Please try again."
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
