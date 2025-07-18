#################################################################################
#
# Makefile to build the project
#
#################################################################################

PROJECT_NAME = Pokemon-Battle-Game
REGION = eu-west-2
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip

## Create python interpreter environment.
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> check python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up VirtualEnv."
	( \
	    $(PIP) install -q virtualenv virtualenvwrapper; \
	    virtualenv venv --python=$(PYTHON_INTERPRETER); \
	)

# Define utility variable to help calling Python from the virtual environment
ACTIVATE_ENV := source venv/bin/activate

# Execute python related functionalities from within the project's environment
define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

## Build the environment requirements
requirements: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)

################################################################################################################
# Set Up
## Install bandit
bandit:
	$(call execute_in_env, $(PIP) install bandit)

## Install black
black:
	$(call execute_in_env, $(PIP) install black)

## Install flake8
flake8:
	$(call execute_in_env, $(PIP) install flake8)

## Install coverage
coverage:
	$(call execute_in_env, $(PIP) install pytest-cov)

## Install pip-audit
pip-audit:
	$(call execute_in_env, $(PIP) install pip-audit)	

## Set up dev requirements (bandit, black & coverage)
dev-setup: bandit black coverage pip-audit flake8

# Build / Run

## Run the security test (bandit)
security-test:
	$(call execute_in_env, bandit -lll */*.py *c/*/*.py)

## Run the black code check
run-black:
	$(call execute_in_env, black --line-length 79 ./src/*/*.py ./test/*/*.py)

## Run flake8 code check
run-flake8:
	$(call execute_in_env, flake8  ./src/*/*.py ./test/*/*.py)	

## Run the unit tests
unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -vvvrP)

## Run the coverage check
check-coverage:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest --cov=src --cov-report=term-missing --cov-report=html)

## Run pip audit
run-pip-audit:
	$(call execute_in_env, pip-audit)


## Run all checks
run-checks: security-test run-black unit-test check-coverage run-flake8 run-pip-audit