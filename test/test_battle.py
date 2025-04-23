# from src.battle import Battle
# from src.pokemon import FirePokemon
# from src.pokemon import WaterPokemon
# from src.pokemon import GrassPokemon


# def test_battle_has_first_pokemon():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = WaterPokemon("Voda", 60, 5, "hurricane")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     assert test_battle.pokemon_1.name == "Infernus"
#     assert test_battle.pokemon_1.hit_points == 30
#     assert test_battle.pokemon_1.attack_damage == 2
#     assert test_battle.pokemon_1.move == "flamethrow"


# def test_battle_has_second_pokemon():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = WaterPokemon("Voda", 60, 5, "hurricane")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     assert test_battle.pokemon_2.name == "Voda"
#     assert test_battle.pokemon_2.hit_points == 60
#     assert test_battle.pokemon_2.attack_damage == 5
#     assert test_battle.pokemon_2.move == "hurricane"


# def test_battle_has_turn_counter():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = WaterPokemon("Voda", 60, 5, "hurricane")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     assert test_battle.pokemon_1_turn is True


# def test_battle_has_take_one_turn():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = WaterPokemon("Voda", 60, 5, "hurricane")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     test_battle.take_turn()
#     assert test_battle.pokemon_1_turn is False
#     assert test_pokemon_02.hit_points == 59


# def test_battle_has_take_multiple_turns():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = WaterPokemon("Voda", 60, 5, "hurricane")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     test_battle.take_turn()
#     test_battle.take_turn()
#     test_battle.take_turn()
#     test_battle.take_turn()
#     test_battle.take_turn()
#     test_battle.take_turn()
#     assert test_battle.pokemon_1_turn is True
#     assert (
#         test_pokemon_01.hit_points == 7.5
# or
# test_pokemon_01.hit_points == 3.75
#     )
#     assert (
#         test_pokemon_02.hit_points == 57
# or
# test_pokemon_02.hit_points == 56.5
#     )


# def test_battle_has_get_first_pokemon_winner():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = WaterPokemon("Voda", 60, 5, "hurricane")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     winner = test_battle.get_winner()
#     assert winner.name == "Voda"


# def test_battle_has_get_second_pokemon_winner():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = GrassPokemon("Herbus", 45, 3, "grow")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     winner = test_battle.get_winner()
#     assert winner.name == "Infernus"


# def test_batttle_str_method_return_expected_output():
#     test_pokemon_01 = FirePokemon("Infernus", 30, 2, "flamethrow")
#     test_pokemon_02 = GrassPokemon("Herbus", 45, 3, "grow")
#     test_battle = Battle(test_pokemon_01, test_pokemon_02)
#     expected_output = (
#         "Battle between:\n" "Infernus\n" "Herbus\n" "Next turn: Infernus"
#     )
#     assert str(test_battle) == expected_output
