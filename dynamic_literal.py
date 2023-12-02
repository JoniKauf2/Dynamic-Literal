import uuid
from typing import Literal, Callable
from enum import Enum

def literalize(*values: str) -> Literal['*values']:
    """
    Creates a new Literal with the given values.\n
    This only changes the runtime type of the the Literal.
    This was designed for libraries, more specifically for discord.py,
    that use type hinting to type check arguments. This allows the 
    programmer to define constants easily and turn them into a Literal
    for easy type hinting and more maintainability.
    """
    class LiteralElem(Enum):
        ELEM = values
    
    literal = Literal[LiteralElem.ELEM]
    literal.__args__ = values

    return literal
