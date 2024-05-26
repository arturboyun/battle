import pytest
from src.domain.characters.hero import Hero
from src.domain.inventory import Inventory


def test_hero_initialization_with_default_inventory():
    hero = Hero("John", 100)
    assert hero.name == "John"
    assert hero.health == 100
    assert isinstance(hero.inventory, Inventory)


def test_hero_initialization_with_custom_inventory_type_error():
    with pytest.raises(TypeError):
        Hero("John", 100, "inventory")


def test_hero_initialization_with_custom_inventory():
    inventory = Inventory()
    hero = Hero("Jane", 150, inventory)
    assert hero.name == "Jane"
    assert hero.health == 150
    assert hero.inventory is inventory
