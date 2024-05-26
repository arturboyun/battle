from src.domain.weapon import Weapon
from .character import Character


class Enemy(Character):
    """
    This class represents an enemy in the game
    """

    race = "Orc"

    def __init__(self, name: str, health: int, weapon: Weapon):
        super().__init__(name, health)
        self.weapon = weapon
