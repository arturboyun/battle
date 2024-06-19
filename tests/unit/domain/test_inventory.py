from uuid import UUID, uuid4

import pytest

from src.battle.domain.inventory import Inventory
from src.battle.domain.item import Item


@pytest.fixture
def items():
    return {uuid4(): Item("Sword", 50.0), uuid4(): Item("Shield", 30.0)}


def test_inventory_init(items: dict[UUID, Item]):
    inventory = Inventory(items)
    assert id(inventory.items) != id(items)
    assert all(isinstance(key, UUID) for key in inventory.items.keys())
    assert all(isinstance(value, Item) for value in inventory.items.values())
    assert inventory.items is not items
    assert inventory.items == items


def test_inventory_wrong_init():
    with pytest.raises(TypeError):
        Inventory("items")
    with pytest.raises(TypeError):
        Inventory({1: Item("Sword", 50.0)})
    with pytest.raises(TypeError):
        Inventory({uuid4(): 1})
    with pytest.raises(TypeError):
        Inventory({uuid4(): Item("Sword", 50.0), 1: Item("Shield", 30.0)})
    with pytest.raises(TypeError):
        Inventory({uuid4(): Item("Sword", 50.0), uuid4(): 1})
    with pytest.raises(TypeError):
        Inventory(
            {
                uuid4(): Item("Sword", 50.0),
                uuid4(): Item("Shield", 30.0),
                1: Item("Axe", 20.0),
            }
        )
    with pytest.raises(TypeError):
        Inventory(
            {
                uuid4(): Item("Sword", 50.0),
                uuid4(): Item("Shield", 30.0),
                uuid4(): 1,
            }
        )


def test_inventory_add_item():
    inventory = Inventory()
    item = Item("Axe", 20.0)
    inventory.add_item(item)
    assert item in inventory.items.values()


def test_inventory_get_item():
    inventory = Inventory()
    item = Item("Axe", 20.0)
    item_id = inventory.add_item(item)
    item = inventory.get_item(item_id)
    assert item is not None
    assert item.id != item_id
    assert item.name == "Axe"
    assert item.price == 20.0
    assert isinstance(item, Item)


def test_inventory_remove_item():
    inventory = Inventory()
    item = Item("Axe", 20.0)
    item_id = inventory.add_item(item)
    assert inventory.remove_item(item_id) == item
    assert item not in inventory.items.values()


def test_inventory_str():
    inventory = Inventory()
    assert str(inventory) == repr(inventory)


def test_inventory_repr():
    inventory = Inventory()
    assert repr(inventory) == f"Inventory(items={inventory.items})"
