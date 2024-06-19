from uuid import UUID, uuid4


class Item:
    """
    Item class
    """

    def __init__(
        self, name: str, price: float | int, *, id_: UUID | None = None
    ):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a float")

        if price < 0:
            raise ValueError("Price must be greater than or equal to 0")
        if name is None or not name.strip():
            raise ValueError("Name must not be empty")

        self._id = id_ if id_ is not None else uuid4()
        self._name = name
        self._price = price if isinstance(price, float) else float(price)

    @property
    def id(self):
        """Returns the id of the item"""
        return self._id

    @property
    def price(self):
        """Returns the price of the item"""
        return self._price

    @property
    def name(self):
        """Returns the name of the item"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the name of the item"""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, price={self.price})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Item):
            return False
        return self.name == value.name and self.price == value.price
