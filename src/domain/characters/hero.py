from src.domain.inventory import Inventory
from .character import Character


class Hero(Character):
    """
    This class represents the hero of the game
    """

    __slots__ = ["_inventory"]

    def __init__(self, name: str, health: int, inventory: Inventory | None = None):
        super().__init__(name, health)

        if inventory is None:
            inventory = Inventory()
        if not isinstance(inventory, Inventory):
            raise TypeError("inventory must be an instance of Inventory")

        self._inventory = inventory

    @property
    def inventory(self) -> Inventory:
        """
        Returns the inventory of the hero
        """
        return self._inventory
