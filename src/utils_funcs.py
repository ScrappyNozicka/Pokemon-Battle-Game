from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup
from pokemon import FirePokemon, WaterPokemon, GrassPokemon, NormalPokemon


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
        return user_input


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
    name = pokemon_dict["Name"]
    type_ = pokemon_dict["Type"]
    hit_points = int(pokemon_dict["Hitpoints"])
    attack_damage = int(pokemon_dict["Damage"])
    move = pokemon_dict["Move"]

    if type_ == "Fire":
        return FirePokemon(name, hit_points, attack_damage, move)
    elif type_ == "Water":
        return WaterPokemon(name, hit_points, attack_damage, move)
    elif type_ == "Grass":
        return GrassPokemon(name, hit_points, attack_damage, move)
    elif type_ == "Normal":
        return NormalPokemon(name, hit_points, attack_damage, move)
    else:
        raise ValueError(f"Unknown Pokémon type: {type_}")


def get_pokemon_data(id_num):
    data = pokemon_data_reader()
    for row in data:
        if row.get("Id") == str(id_num):
            return create_pokemon_instance(row)
    return None
