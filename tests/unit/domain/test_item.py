import pytest
from src.domain.item import Item
from uuid import UUID


def test_item_initialization():
    name = "Test Item"
    price = 10.99
    item = Item(name, price)
    assert item.name == name
    assert item.price == price
    assert isinstance(item.id, UUID)


def test_item_wrong_initialization():
    with pytest.raises(TypeError):
        Item(1, 10.99)
    with pytest.raises(TypeError):
        Item("Test Item", "10.99")
    with pytest.raises(ValueError):
        Item("", 10.99)
    with pytest.raises(ValueError):
        Item("Test Item", -10.99)


def test_item_name_setter():
    item = Item("Test Item", 10.99)
    new_name = "New Item Name"
    item.name = new_name
    assert item.name == new_name


def test_item_name_setter_wrong_type():
    item = Item("Test Item", 10.99)
    with pytest.raises(TypeError):
        item.name = 1


def test_item_equality():
    item1 = Item("Test Item", 10.99)
    item2 = Item("Test Item", 10.99)
    item3 = Item("Different Item", 20.99)
    assert item1 == item2
    assert item1 != item3
    assert item1 != 1


def test_item_repr():
    item = Item("Test Item", 10.99)
    assert repr(item) == f"Item(id={item.id}, name='Test Item', price=10.99)"


def test_item_str():
    item = Item("Test Item", 10.99)
    assert str(item) == repr(item)
