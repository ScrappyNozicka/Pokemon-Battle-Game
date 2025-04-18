from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup
from pokemon import FirePokemon, WaterPokemon, GrassPokemon, NormalPokemon
import random
from move import Move
from trainer import Trainer


def input_manager(prompt):
    """
    Handler of empty input in main script of Password Manager.

    Args:
        promt: User input.
    """

    while True:
        user_input = input(prompt)
        if not user_input:
            print("Input cannot be empty, please try again.")
            continue
        return user_input.strip()


def pokemon_data_reader():
    with open("pokemon_data.md", "r", encoding="utf-8") as file:
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
    else:
        raise ValueError(f"Unknown Pokémon type: {type_}")


def catch_random_pokemon():
    data = pokemon_data_reader()
    chosen = random.choice(data)
    pokemon = create_pokemon_instance(chosen)
    print(f"You caught a wild {pokemon.name}!")
    return pokemon


def get_pokemon_data(id_num):
    data = pokemon_data_reader()
    for row in data:
        if row.get("Id") == str(id_num):
            return create_pokemon_instance(row)
    return None

def trainer_setup(role):
    trainer_name = input_manager(
        f"What's the {role}'s trainer name?\n"
    )
    trainer = Trainer(trainer_name)
    print(trainer)
    
    if trainer.space_on_belt == 6:
        first_pokemon_selection = input_manager(f"{role.capitalize()}, do you want to [s]elect your first pokemon or choose one at [r]andom?\n")
        while first_pokemon_selection.lower() not in "sr":
            first_pokemon_selection = input_manager(
                "Invalid input. Please specify: "
                "[s]elect your pokemon or choose [r]andom pokemon.\n"
            )
        if first_pokemon_selection.lower() == "s":
            while True:
                pokemon_id = input_manager("What's the pokemon id? (or type 'q' to cancel)\n\n")
                if pokemon_id.lower() == 'q':
                    print("Cancelled Pokémon selection.")
                    break
                pokemon = get_pokemon_data(pokemon_id)
                if pokemon:
                    trainer.throw_pokeball(pokemon)
                    break
                else:
                    print("Pokemon not found, please try again.")
        elif first_pokemon_selection.lower() == "r":
            random_pokemon = catch_random_pokemon()
            trainer.throw_pokeball(random_pokemon)


    while trainer.belt_space():
        further_selection = input_manager(f"{role.capitalize()}, do you want to catch further pokemon? [y/n]\n")
        while further_selection.lower() not in "yn":
            further_selection = input_manager(
                "Invalid input. Please specify: "
                "[y] to catch further pokemon or [n] to start the battle.\n"
            )
        if further_selection.lower() == "y": 
            pokemon_selection = input_manager(f"{role.capitalize()}, do you want to [s]elect your pokemon or choose one at [r]andom?\n")
            while pokemon_selection.lower() not in "sr":
                pokemon_selection = input_manager(
                "Invalid input. Please specify: "
                "[s]elect your pokemon or choose [r]andom pokemon.\n"
            )
            if pokemon_selection.lower() == "s":
                while True:
                    pokemon_id = input_manager("What's the pokemon id? (or type 'q' to cancel)\n")
                    if pokemon_id.lower() == 'q':
                        print("Cancelled Pokémon selection.")
                        break
                    pokemon = get_pokemon_data(pokemon_id)
                    if pokemon:
                        trainer.throw_pokeball(pokemon)
                        break
                    else:
                        print("Pokemon not found, please try again.")
            if pokemon_selection.lower() == "r":
                random_pokemon = catch_random_pokemon()
                trainer.throw_pokeball(random_pokemon)
        if further_selection.lower() == "n":
            print("thank you for your choice.\n")
            break
    return trainer