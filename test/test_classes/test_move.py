from src.classes.move import Move


def test_move_has_name():
    test_move = Move("Attack", 10, 5)

    assert test_move.name == "Attack"


def test_move_has_damage():
    test_move = Move("Attack", 10, 5)

    assert test_move.damage == 10


def test_move_has_max_powerpoints():
    test_move = Move("Attack", 10, 5)

    assert test_move.max_powerpoints == 5


def test_move_has_powerpoints():
    test_move = Move("Attack", 10, 5)

    assert test_move.powerpoints == 5


def test_move_use_of_one_decreases_powerpoints_by_one():
    test_move = Move("Attack", 10, 5)

    test_move.use()

    assert test_move.powerpoints == 4
    assert test_move.max_powerpoints == 5


def test_move_use_of_one_returns_true_when_powerpoints_available():
    test_move = Move("Attack", 10, 5)

    assert test_move.use() is True


def test_move_use_multi_times_decreases_powerpoints_multi_times():
    test_move = Move("Attack", 10, 5)

    test_move.use()
    test_move.use()
    test_move.use()

    assert test_move.powerpoints == 2
    assert test_move.max_powerpoints == 5


def test_move_use_max_times_decreases_powerpoints_to_zero():
    test_move = Move("Attack", 10, 5)

    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()

    assert test_move.powerpoints == 0
    assert test_move.max_powerpoints == 5


def test_move_use_over_max_times_returns_false_when_no_powerpoints_available():
    test_move = Move("Attack", 10, 5)

    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()

    assert test_move.use() is False


def test_pokeball_str_method_return_expected_output_when_empty():
    test_move = Move("Attack", 10, 5)

    expected_output = "Attack (AP: 10, PP: 5)"

    assert str(test_move) == expected_output
