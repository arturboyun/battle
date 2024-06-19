from src.battle.domain.weapon import Weapon


from .character import Character


class Enemy(Character):
    """
    This class represents an enemy in the game
    """

    def __init__(self, name: str, health: int, weapon: Weapon):
        super().__init__(name, health)
        if not isinstance(weapon, Weapon):
            raise TypeError("weapon must be an instance of Weapon")
        self._weapon = weapon
