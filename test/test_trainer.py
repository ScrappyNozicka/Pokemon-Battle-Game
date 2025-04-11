from src.trainer import Trainer
from src.pokemon import Pokemon
from src.pokeball import Pokeball


def test_trainer_has_empty_belt():
    test_trainer = Trainer()
    for pokeball in test_trainer.belt:
        assert type(pokeball) is Pokeball
    assert len(test_trainer.belt) == 6
    for pokeball in test_trainer.belt:
        assert pokeball.Pokemon is None


def test_throw_pokeball_catches_pokemon_if_pokeballs_available():
    test_trainer = Trainer()
    test_pokemon = Pokemon("Bob", 3, 4, "move")
    test_trainer.throw_pokeball(test_pokemon)
    first_pokeball = test_trainer.belt[0]
    assert first_pokeball.Pokemon == test_pokemon


# test catching multiple pokemon subsequently
def test_throw_pokeball_catches_multiple_pokemon_subsequently():
    test_trainer = Trainer()
    test_pokemon1 = Pokemon("Bob", 3, 4, "move")
    test_pokemon2 = Pokemon("Humphrey", 7, 4, "bash")
    test_trainer.throw_pokeball(test_pokemon1)
    test_trainer.throw_pokeball(test_pokemon2)
    first_pokeball = test_trainer.belt[0]
    second_pokeball = test_trainer.belt[1]
    assert first_pokeball.Pokemon == test_pokemon1
    assert second_pokeball.Pokemon == test_pokemon2


def test_throw_pokeball_catch_pokemon_while_some_pokemon_caught_already():
    test_pokemon1 = ("Bob", 3, 4, "move")
    test_trainer = Trainer(prefilled_pokemon=test_pokemon1)
    test_pokemon2 = Pokemon("Humphrey", 7, 4, "bash")
    test_trainer.throw_pokeball(test_pokemon2)
    first_pokeball = test_trainer.belt[0]
    assert first_pokeball.Pokemon == test_pokemon1
    second_pokeball = test_trainer.belt[1]
    assert second_pokeball.Pokemon == test_pokemon2


# def test throw pokeball does not catch pokemon if no available pokeballs


# def test_throw_pokeball_does_not_catch_pokemon_if_no_available_pokeballs():
#     test_pokemon1 = "Bob", 3, 4, "move"
#     test_pokemon2 = "Humphrey", 7, 4, "bash"
#     test_pokemon3 = "Adalbert", 3, 3, "pokemon knowledge"
#     test_pokemon4 = "Redvers", 6, 8, "stuff"
#     test_pokemon5 = "Algernon", 2, 9, "bite"
#     test_pokemon6 = "Pancrazio", 5, 6, "gesturing"
#     test_trainer = Trainer(
#         prefilled_pokemon=[
#             test_pokemon1,
#             test_pokemon2,
#             test_pokemon3,
#             test_pokemon4,
#             test_pokemon5,
#             test_pokemon6,
#         ]
#     )
#     test_pokemon7 = ("Nebudchanezzar", 7, 4, "dreaming")
#     with pytest.raises(
#         NoEmptyPokeballError, match="Sorry no empty pokeballs available"
#     ):
#         test_trainer.throw_pokeball(test_pokemon7)
