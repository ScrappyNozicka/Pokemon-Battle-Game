from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup


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
    console = Console()
    with open("pokemon_data.md", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")

    table_html = soup.find("table")
    headers = [th.text for th in table_html.find_all("th")]
    rows = [
        [td.text for td in tr.find_all("td")]
        for tr in table_html.find_all("tr")[1:]
    ]

    table = Table(title="Pokemon Stats")

    for header in headers:
        table.add_column(header)

    for row in rows:
        table.add_row(*row)

    console.print(table)
    return table
