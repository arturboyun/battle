from uuid import UUID

import pytest


from src.battle.domain.weapon import Weapon


def test_weapon_creation():
    """
    Test that a weapon can be created with the correct attributes
    """
    weapon = Weapon(
        name="Iron Sword", weapon_type="Sword", damage=10, price=10
    )
    assert weapon.name == "Iron Sword"
    assert weapon.weapon_type == "Sword"
    assert weapon.damage == 10
    assert weapon.id is not None
    assert isinstance(weapon.id, UUID)


def test_weapon_creation_invalid_attributes():
    with pytest.raises(ValueError):
        Weapon(name="", weapon_type="Sword", damage=10, price=10)
    with pytest.raises(ValueError):
        Weapon(name="Iron Sword", weapon_type="Sword", damage=10, price=-10)
    with pytest.raises(TypeError):
        Weapon(name="Iron Sword", weapon_type=123123, damage=10, price=0)
    with pytest.raises(TypeError):
        Weapon(name="Iron Sword", weapon_type="Test", damage="10", price=0)
