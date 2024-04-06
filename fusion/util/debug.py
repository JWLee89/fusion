from typing import Any, Callable


def decorate():
    pass


class _FuncDict(dict):
    """A dictionary that accepts only functions as values."""

    def __init__(self, *args, **kwargs) -> None:
        return super().__init__(*args, **kwargs)

    def __setitem__(self, name: Any, value: Callable) -> None:
        """This function is used to ensure that only
        functions are added to the dictionary

        Args:
            name (Any): A hashable object
            value (Callable): A value to set.

        Raises:
            TypeError: If the value is not a function,
            return an error.
        """
        if not isinstance(value, Callable):
            raise TypeError(f"Expected Callable, got {type(value)}")
        return super().__setitem__(name, value)


class Debugger:
    __globally_observed = _FuncDict()

    def __init__(self, debug: bool) -> None:
        self.debug = debug

    def register(self, func: Callable, name: str = None) -> None:
        """Register a function. The function should be

        Args:
            func (Callable): The function to register
        """
        if name is None:
            name_to_register = func.__name__
        if name_to_register in self.__globally_observed:
            raise ValueError(f"{name_to_register} already exists.")
        self.__globally_observed[name_to_register] = func

    def pre_hook(self, func: Callable) -> None:
        """_summary_

        Args:
            func (Callable): _description_
        """
