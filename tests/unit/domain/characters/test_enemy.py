import pytest
from domain.weapon import Weapon
from domain.characters.enemy import Enemy


def test_enemy_initialization():
    name = "Goblin"
    health = 100
    weapon = Weapon("test", "test", 10, 20)
    enemy = Enemy(name, health, weapon)

    assert enemy.name == name
    assert enemy.health == health
    assert enemy.weapon == weapon


def test_enemy_initialization_invalid_weapon():
    name = "Goblin"
    health = 100
    weapon = "Axe"  # Invalid weapon
    with pytest.raises(TypeError):
        Enemy(name, health, weapon)
