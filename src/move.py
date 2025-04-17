class Move:
    def __init__(self, name, damage, powerpoints):
        self.name = name
        self.damage = damage
        self.powerpoints = powerpoints

    def use(self):
        if self.powerpoints > 0:
            self.powerpoints -= 1
            return True
        return False

    def __str__(self):
        return f"{self.name} (AP: {self.damage}, PP: {self.powerpoints})"
