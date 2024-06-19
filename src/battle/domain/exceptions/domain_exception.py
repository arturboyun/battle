class DomainException(Exception):
    """
    Base class for domain exceptions
    """

    def __init__(self, message: str):
        self._message = message
        super().__init__(self.message)

    @property
    def message(self):
        """
        Returns the exception message
        """
        return self._message
