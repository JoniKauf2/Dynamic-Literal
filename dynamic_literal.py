import uuid
from typing import Literal, Callable
from enum import Enum

def literalize(*values: str, anti_interning_method: Callable = lambda: str(uuid.uuid4()), **method_args) -> Literal['*values']:
    """
    Creates a new Literal with the given values.\n
    This only changes the runtime type of the the Literal, while
    the static type is based off the `anti_interning_method` and
    cannot change. Therefore it has very limited use and is not designed
    for general purpose use.\n
    This was designed for libraries, more specifically for discord.py,
    that use type hinting to type check arguments. This allows the 
    programmer to define constants easily and turn them into a Literal
    for easy type hinting and more maintainability.
    """
    class LiteralElem(Enum):
        ELEM = anti_interning_method(**method_args)
    
    literal = Literal[LiteralElem.ELEM]
    literal.__args__ = values

    return literal
