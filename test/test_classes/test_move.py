from src.classes.move import Move


def test_move_has_name():
    """
    Test that verifies if a Move object
        has the correct 'name' attribute.
    Ensures the 'name' attribute is correctly initialized
        when a Move is created.
    """
    test_move = Move("Attack", 10, 5)

    assert test_move.name == "Attack"


def test_move_has_damage():
    """
    Test that verifies if a Move object
        has the correct 'damage' attribute.
    Ensures the 'damage' attribute is correctly initialized
        when a Move is created.
    """
    test_move = Move("Attack", 10, 5)

    assert test_move.damage == 10


def test_move_has_max_powerpoints():
    """
    Test that verifies if a Move object
        has the correct 'max_powerpoints' attribute.
    Ensures the 'max_powerpoints' attribute is correctly initialized
        when a Move is created.
    """
    test_move = Move("Attack", 10, 5)

    assert test_move.max_powerpoints == 5


def test_move_has_powerpoints():
    """
    Test that verifies if a Move object has
        the correct 'powerpoints' attribute.
    Ensures the 'powerpoints' attribute is initialized
        with the value of 'max_powerpoints' when a Move is created.
    """
    test_move = Move("Attack", 10, 5)

    assert test_move.powerpoints == 5


def test_move_use_of_one_decreases_powerpoints_by_one():
    """
    Test that verifies if using a Move decreases
        the 'powerpoints' by one.
    Ensures that after using a Move once,
        the 'powerpoints' are reduced by 1,
            but 'max_powerpoints' remains unchanged.
    """
    test_move = Move("Attack", 10, 5)

    test_move.use()

    assert test_move.powerpoints == 4
    assert test_move.max_powerpoints == 5


def test_move_use_of_one_returns_true_when_powerpoints_available():
    """
    Test that verifies if the 'use' method returns True
        when there are available powerpoints.
    Ensures that using the Move returns True
        when there are enough powerpoints for a move.
    """
    test_move = Move("Attack", 10, 5)

    assert test_move.use() is True


def test_move_use_multi_times_decreases_powerpoints_multi_times():
    """
    Test that verifies if using a Move multiple times
        decreases 'powerpoints' correctly.
    Ensures that the 'powerpoints' attribute is reduced by 1
        for each use and 'max_powerpoints' remains the same.
    """
    test_move = Move("Attack", 10, 5)

    test_move.use()
    test_move.use()
    test_move.use()

    assert test_move.powerpoints == 2
    assert test_move.max_powerpoints == 5


def test_move_use_max_times_decreases_powerpoints_to_zero():
    """
    Test that verifies if using a Move the maximum number of times
        decreases 'powerpoints' to zero.
    Ensures that after using a Move as many times
        as there are powerpoints, the 'powerpoints' reach zero.
    """
    test_move = Move("Attack", 10, 5)

    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()

    assert test_move.powerpoints == 0
    assert test_move.max_powerpoints == 5


def test_move_use_over_max_times_returns_false_when_no_powerpoints_available():
    """
    Test that verifies if the 'use' method returns False
        when there are no powerpoints available.
    Ensures that after all powerpoints are used,
        further attempts to use the Move return False.
    """
    test_move = Move("Attack", 10, 5)

    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()
    test_move.use()

    assert test_move.use() is False


def test_pokeball_str_method_return_expected_output_when_empty():
    """
    Test the string representation of a Move object.
    Ensures that the string output of the Move object
        correctly reflects the 'name', 'damage', and 'powerpoints'.
    """
    test_move = Move("Attack", 10, 5)

    expected_output = "Attack (AP: 10, PP: 5)"

    assert str(test_move) == expected_output
