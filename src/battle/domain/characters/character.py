from src.battle.domain.weapon import Weapon, fists


class Character:
    """
    This class represents a character in the game
    """

    __slots__ = ["_name", "_health", "_max_health", "_weapon"]

    def __init__(self, name: str, health: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(health, int):
            raise TypeError("Health must be an integer")
        if health < 0:
            raise ValueError("Health must be greater or equal to 0")

        self._name = name
        self._health = health
        self._max_health = health
        self._weapon = fists

    @property
    def name(self) -> str:
        """
        Get the name of the character
        """
        return self._name

    @property
    def health(self) -> int:
        """
        Get the health of the character
        """
        return self._health

    @health.setter
    def health(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Health must be an integer")
        if value < 0:
            raise ValueError("Health must be greater or equal to 0")
        if value > self._max_health:
            raise ValueError(
                f"Health must be less or equal to max health ({self._max_health})"
            )
        self._health = value

    @property
    def max_health(self) -> int:
        """
        Get the maximum health of the character
        """
        return self._max_health

    @property
    def weapon(self) -> "Weapon":
        """
        Get the equipped weapon of the character
        """
        return self._weapon

    @weapon.setter
    def weapon(self, value: "Weapon"):
        if not isinstance(value, Weapon):
            raise TypeError("Weapon must be a Weapon instance")
        self._weapon = value

    def attack(self, target: "Character") -> "Character":
        """
        Attack another character
        """
        final_health = target.health - self.weapon.damage
        target.health = final_health if final_health >= 0 else 0
        return target
