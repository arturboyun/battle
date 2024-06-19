from uuid import UUID, uuid4

from src.battle.domain.item import Item

type ItemsList = dict[UUID, Item]


class Inventory:
    """
    Represents an inventory that holds items.
    """

    def __init__(self, items: ItemsList | None = None):
        if items is None:
            items = {uuid4(): Item(name="Fists", price=0)}
        if not isinstance(items, dict):
            raise TypeError("Items must be a dictionary")
        if not all(isinstance(key, UUID) for key in items.keys()):
            raise TypeError("Keys must be UUIDs")
        if not all(isinstance(value, Item) for value in items.values()):
            raise TypeError("Values must be Items")

        self._items: ItemsList = items.copy()

    @property
    def items(self) -> ItemsList:
        """
        Returns a list of the items in the inventory.
        """
        return self._items

    def add_item(self, item: Item) -> UUID:
        """
        Adds an item to the inventory.
        """
        id_ = uuid4()
        self._items[id_] = item
        return id_

    def get_item(self, id_: UUID) -> Item | None:
        """
        Returns an item from the inventory by its ID.
        """
        return self._items.get(id_, None)

    def remove_item(self, id_: UUID) -> Item | None:
        """
        Removes and returns an item from the inventory by its ID.
        """
        return self._items.pop(id_, None)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Inventory(items={self._items})"
