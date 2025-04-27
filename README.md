# Pokemon Battle Game

## Description
Terminal based pokemon battle game utilising python script.

It allows two players to list and view available pokemon, select up to six of them and battle until one player's pokemon have all fainted. 

Each battle allows for:
 - Swapping between pokemon during battle.
 - Selecting from three different Pokemon moves each round.
 - Accounts for PoperPoints being decresed when move is being used.
 - Accounts for strengths and weaknesses against specific types of each Pokemon.


## Technologies used
- **Python:** Version 3.12
- **Data Formats:** MD for storing list of available pokemon
- **Automation Tools:**  CI/CD for deployment

## Installation

### Prerequisites
- [Python](https://www.python.org/downloads/) - version 3.12 or above
- [Make](https://www.gnu.org/software/make/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ScrappyNozicka/Pokemon-Battle-Game
   cd pokemon-battle-game
2. Install dependencies:
    - `create-environment`(automated by `requirements`): Creates a Python virtual environment.
        ```bash
        make create-environment
    - `requirements`: Installs the project dependencies from requirements.txt.
        ```bash
        make requirements
    - `dev-setup`: Installs development tools(bandit, black, flake8, pytest-cov, and pip-audit)
        ```bash
        make dev-setup
    - `run-checks`: Runs security tests, code checks, unit tests, coverage analysis
        ```bash
        make run-checks