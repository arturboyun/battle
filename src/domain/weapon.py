from .item import Item


class Weapon(Item):
    """
    This class represents a weapon
    """

    def __init__(self, name: str, weapon_type: str, damage: int, price: float):
        super().__init__(name, price)

        if not isinstance(weapon_type, str):
            raise TypeError("Weapon type must be a string")
        if not isinstance(damage, int):
            raise TypeError("Damage must be an integer")

        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = price


iron_sword = Weapon(name="Iron Sword", weapon_type="Sword", damage=10, price=10)
short_bow = Weapon(name="Short Bow", weapon_type="Bow", damage=5, price=8)
fists = Weapon(name="Fists", weapon_type="Unarmed", damage=2, price=0)
