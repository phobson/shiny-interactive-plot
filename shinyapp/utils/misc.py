from collections.abc import Callable
from typing import Any, TypeVar

from shiny.types import SilentException

T = TypeVar("T", int, float)


def add_numbers(x: T, y: T) -> T:
    return x + y


def try_to_read(shiny_input: Callable, default: Any) -> Any:
    try:
        return shiny_input()
    except SilentException:
        return default
