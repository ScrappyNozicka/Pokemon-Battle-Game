from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup
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
import random
from src.classes.move import Move
from src.classes.trainer import Trainer


def input_manager(prompt):
    """
    Handles user input and prevents empty entries.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        str: The user's input, stripped of leading/trailing whitespace.
    """
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Input cannot be empty, please try again.")
            continue
        return user_input.strip()


def pokemon_data_reader(location):
    """
    Reads and parses Pokemon data from a Markdown HTML table.

    Args:
        location (str): The file path of the data source.

    Returns:
        list[dict]: A list of dictionaries representing Pokemon data.
    """
    with open(location, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")

    table_html = soup.find("table")
    headers = [th.text for th in table_html.find_all("th")]
    rows = [
        [td.text for td in tr.find_all("td")]
        for tr in table_html.find_all("tr")[1:]
    ]
    data = [dict(zip(headers, row)) for row in rows]
    return data


def pokemon_table_display(data):
    """
    Displays Pokemon data in a table format using Rich.

    Args:
        data (list[dict]): The Pokemon data to display.

    Returns:
        Table: The rendered Rich Table object.
    """
    console = Console()

    headers = data[0].keys()
    table = Table(title="Pokemon Stats")

    for header in headers:
        table.add_column(header)

    for row in data:
        table.add_row(*[row[col] for col in headers])

    console.print(table)
    return table


def create_pokemon_instance(pokemon_dict):
    """
    Creates a Pokemon object instance from a dictionary of stats.

    Args:
        pokemon_dict (dict): A dictionary with Pokemon attributes.

    Returns:
        Pokemon: An instance of a specific Pokemon subclass.
    """
    pokemon_id = pokemon_dict["Id"]
    name = pokemon_dict["Name"]
    type_ = pokemon_dict["Type"]
    hit_points = int(pokemon_dict["Hitpoints"])

    move_01 = Move(
        pokemon_dict["Move 01"],
        int(pokemon_dict["Damage 01"]),
        int(pokemon_dict["Powerpoints 01"]),
    )
    move_02 = Move(
        pokemon_dict["Move 02"],
        int(pokemon_dict["Damage 02"]),
        int(pokemon_dict["Powerpoints 02"]),
    )
    move_03 = Move(
        pokemon_dict["Move 03"],
        int(pokemon_dict["Damage 03"]),
        int(pokemon_dict["Powerpoints 03"]),
    )

    args = (pokemon_id, name, hit_points, move_01, move_02, move_03)

    if type_ == "Fire":
        return FirePokemon(*args)
    elif type_ == "Water":
        return WaterPokemon(*args)
    elif type_ == "Grass":
        return GrassPokemon(*args)
    elif type_ == "Normal":
        return NormalPokemon(*args)
    elif type_ == "Electric":
        return ElectricPokemon(*args)
    elif type_ == "Fighting":
        return FightingPokemon(*args)
    elif type_ == "Poison":
        return PoisonPokemon(*args)
    elif type_ == "Psychic":
        return PsychicPokemon(*args)
    elif type_ == "Bug":
        return BugPokemon(*args)
    elif type_ == "Ghost":
        return GhostPokemon(*args)
    elif type_ == "Dragon":
        return DragonPokemon(*args)
    elif type_ == "Fairy":
        return FairyPokemon(*args)
    elif type_ == "Ground":
        return GroundPokemon(*args)
    else:
        raise ValueError(f"Unknown Pokemon type: {type_}")


def catch_random_pokemon(location):
    """
    Creates a random Pokemon instance and announces the catch.

    Args:
        location (str): The file path of the Pokemon data.

    Returns:
        Pokemon: The caught Pokemon object.
    """
    data = pokemon_data_reader(location)
    chosen = random.choice(data)
    pokemon = create_pokemon_instance(chosen)
    print(f"You caught a wild {pokemon.name}!")
    return pokemon


def get_pokemon_data(id_num, location):
    """
    Retrieves a specific Pokemon by its ID.

    Args:
        id_num (str): The ID number of the desired Pokemon.
        location (str): The file path of the Pokemon data.

    Returns:
        Pokemon or None: The Pokemon object or None if not found.
    """
    data = pokemon_data_reader(location)
    for row in data:
        if row.get("Id") == str(id_num):
            return create_pokemon_instance(row)
    return None


def trainer_setup(role, location):
    """
    Sets up a trainer by allowing Pokemon selection or random assignment.

    Args:
        role (str): 'challenger' or 'defender'.
        location (str): The file path of the Pokemon data.

    Returns:
        Trainer: The trainer object with selected Pokemon.
    """
    trainer_name = input_manager(f"What's the {role}'s trainer name?\n")
    trainer = Trainer(trainer_name)
    print(trainer)

    while trainer.space_on_belt == 6:
        first_pokemon_selection = input_manager(
            f"{role.capitalize()}, do you want to [s]elect your first pokemon,"
            " choose [r]andom pokemon or [c]ancel?\n"
        )
        if first_pokemon_selection.lower() == "c":
            print("Cancelled Pokemon selection.")
            return trainer
        while first_pokemon_selection.lower() not in "sr":
            first_pokemon_selection = input_manager(
                "Invalid input. Please specify: "
                "[s]elect pokemon, choose [r]andom pokemon or [c]ancel.\n"
            )
            if first_pokemon_selection.lower() == "c":
                print("Cancelled Pokemon selection.")
                return trainer
        if first_pokemon_selection.lower() == "s":
            while True:
                pokemon_id = input_manager(
                    "What's the pokemon id? (or [c]ancel)\n"
                )
                if pokemon_id.lower() == "c":
                    print("Cancelled Pokemon selection.")
                    return trainer
                pokemon = get_pokemon_data(pokemon_id, location)
                if pokemon:
                    trainer.throw_pokeball(pokemon)
                    break
                else:
                    print("Pokemon not found, please try again.")
        elif first_pokemon_selection.lower() == "r":
            random_pokemon = catch_random_pokemon(location)
            trainer.throw_pokeball(random_pokemon)

    while trainer.belt_space():
        print(trainer)
        further_selection = input_manager(
            f"{role.capitalize()}, do you want to catch more pokemon? [y/n]\n"
        )
        while further_selection.lower() not in "yn":
            further_selection = input_manager(
                "Invalid input. Please specify: "
                "[y] to catch more pokemon or [n] to start the battle.\n"
            )
        if further_selection.lower() == "y":
            pokemon_selection = input_manager(
                f"{role.capitalize()}, do you want to [s]elect pokemon, "
                "choose [r]andom pokemon or [c]ancel?\n"
            )
            if pokemon_selection.lower() == "c":
                print("Cancelled Pokemon selection.")
                return trainer
            while pokemon_selection.lower() not in "sr":
                pokemon_selection = input_manager(
                    "Invalid input. Please specify: "
                    "[s]elect pokemon, choose [r]andom pokemon or [c]ancel.\n"
                )
                if pokemon_selection.lower() == "c":
                    print("Cancelled Pokemon selection.")
                    return trainer
            if pokemon_selection.lower() == "s":
                while True:
                    pokemon_id = input_manager(
                        "What's the pokemon id? (or [c]ancel)\n"
                    )
                    if pokemon_id.lower() == "c":
                        print("Cancelled Pokemon selection.")
                        return trainer
                    pokemon = get_pokemon_data(pokemon_id, location)
                    if pokemon:
                        trainer.throw_pokeball(pokemon)
                        break
                    else:
                        print("Pokemon not found, please try again.")
            if pokemon_selection.lower() == "r":
                random_pokemon = catch_random_pokemon(location)
                trainer.throw_pokeball(random_pokemon)
        if further_selection.lower() == "n":
            print("Thank you for your choice.\n\n")
            return trainer
    return trainer


def select_starting_pokemon(trainer):
    """
    Prompts the trainer to choose which Pokemon to send into battle first.

    Args:
        trainer (Trainer): The trainer choosing their Pokemon.

    Returns:
        Pokemon: The selected Pokemon to start the battle.
    """
    while True:
        if trainer.space_on_belt == 6:
            print(f"\n{trainer.name} has chosen no Pokemon, ending the game.")
            break
        print(f"\n{trainer.name}'s available Pokemon:")
        for pokeball in trainer.trainer_belt:
            if not pokeball.is_empty():
                p = pokeball.pokemon
                print(
                    f"{p.pokemon_id}: {p.name}, "
                    f"Type: {p.type}, HP: {p.hit_points}\n"
                )

        selected_id = input_manager(
            f"{trainer.name}, which Pokemon do you send out first?"
        )

        selected_pokemon = trainer.get_pokemon_by_id(selected_id)
        if selected_pokemon:
            return selected_pokemon
        else:
            print("Invalid Pokemon ID. Please try again.")
