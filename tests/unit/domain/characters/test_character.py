import pytest

from src.battle.domain.characters.character import Character
from src.battle.domain.weapon import Weapon


def test_character_initialization():
    character = Character("John", 100)
    assert character.name == "John"
    assert character.health == 100
    assert character.max_health == 100
    assert isinstance(character.weapon, Weapon)


def test_character_initialization_invalid_attributes():
    with pytest.raises(TypeError):
        Character(123, 100)
    with pytest.raises(TypeError):
        Character("John", "100")
    with pytest.raises(ValueError):
        Character("John", -100)


def test_character_attack():
    character1 = Character("John", 100)
    character2 = Character("Enemy", 100)
    character1.weapon = Weapon("Iron Sword", "Sword", 10, 10)
    character1.attack(character2)
    assert character2.health == 90


def test_character_attack_with_zero_health():
    character1 = Character("John", 100)
    character2 = Character("Enemy", 0)
    target = character1.attack(character2)
    assert target.health == 0
    assert target is character2


def test_character_set_health_invalid_value():
    character = Character("John", 100)
    with pytest.raises(TypeError):
        character.health = "100"
    with pytest.raises(ValueError):
        character.health = -100
    with pytest.raises(ValueError):
        character.health = character.max_health + 1


def test_character_equip_weapon():
    character = Character("John", 100)
    weapon = Weapon("Iron Sword", "Sword", 10, 10)
    character.weapon = weapon
    assert character.weapon == weapon


def test_character_equip_weapon_invalid_value():
    character = Character("John", 100)
    with pytest.raises(TypeError):
        character.weapon = "Iron Sword"
