from abc import ABC, abstractmethod
from typing import Generic, TypeVar

InputDto = TypeVar("InputDto")
OutputDto = TypeVar("OutputDto")


class Interactor(ABC, Generic[InputDto, OutputDto]):
    """
    Interactor is an abstract class that defines the interface for all interactors.

    An interactor is a class that contains the business logic of a use case.
    It is responsible for executing the use case
    and returning the result to the caller.
    The interactor should not contain any code that is specific to the
    user interface or the data access layer.
    This allows the interactor to be reused in different contexts.

    The execute method is the main method of the interactor.
    It should contain the business logic of the use case. The execute method should be
    called by the application layer to execute the use case.
    """

    @abstractmethod
    def __call__(self, data: InputDto) -> OutputDto:
        """
        Executes the use case.
        """
        raise NotImplementedError
