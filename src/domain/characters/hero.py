from src.domain.inventory import Inventory
from .character import Character


class Hero(Character):
    """
    This class represents the hero of the game
    """

    __slots__ = ["inventory"]

    def __init__(self, name: str, health: int, inventory: Inventory | None = None):
        super().__init__(name, health)

        if inventory is None:
            self.inventory = Inventory()
