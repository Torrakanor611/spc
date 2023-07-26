"""Factory for creating a load data class"""

from typing import Any, Callable

from pluginInterface import PluginInterface

inputdata_creation_funcs: dict[str, Callable[..., PluginInterface]] = {}


def register(inputdata_type: str, creator: Callable[..., PluginInterface]) -> None:
    """Register a new load data type."""
    inputdata_creation_funcs[inputdata_type] = creator


def unregister(inputdata_type: str) -> None:
    """Unregister a load data type."""
    inputdata_creation_funcs.pop(inputdata_type, None)


def create(arguments: dict[str, Any]) -> PluginInterface:
    """Create a load data of a specific type, given JSON data."""
    args_copy = arguments.copy()
    inputdata_type = args_copy.pop("type")
    try:
        creator_func = inputdata_creation_funcs[inputdata_type]
    except KeyError:
        raise ValueError(f"unknown character type {inputdata_type!r}") from None
    return creator_func(**args_copy)