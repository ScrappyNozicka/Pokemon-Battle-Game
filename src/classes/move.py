class Move:
    """
    Represents a move that a Pokemon can use in battle.

    Attributes:
        name (str): The name of the move.
        damage (int): The damage (attack power) the move deals.
        max_powerpoints (int):
            The maximum number of times the move can be used.
        powerpoints (int): The current remaining uses of the move.
    """

    def __init__(self, name, damage, powerpoints):
        """
        Initializes a Move instance with its name, damage, and power points.

        Args:
            name (str): The name of the move.
            damage (int): The amount of damage the move can deal.
            powerpoints (int): The number of times the move can be used.
        """
        self.name = name
        self.damage = damage
        self.max_powerpoints = powerpoints
        self.powerpoints = powerpoints

    def use(self):
        """
        Attempts to use the move, reducing its available PowerPoints.

        Returns:
            bool:   
                True if the move was successfully used,
                    False if no PowerPoints remain.
        """
        if self.powerpoints > 0:
            self.powerpoints -= 1
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of the move.

        Returns:
            str: A string showing the move's name,
            attack power (AP), and remaining PowerPoints (PP).
        """
        return f"{self.name} (AP: {self.damage}, PP: {self.powerpoints})"
