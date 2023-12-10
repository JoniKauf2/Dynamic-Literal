import uuid
from typing import Literal, Callable
from enum import Enum

def literalize(*values: str | Iterable[str]) -> Literal['*values']:
    """
    Creates a new Literal with the given values.
    This only changes the runtime type of the the Literal.
    This was designed for libraries, more specifically for discord.py,
    that use type hinting to type check arguments. This allows the 
    programmer to define constants easily and turn them into a Literal
    for easy type hinting and more maintainability.
    """
    
    flattened = []
    for val in values:
        if isinstance(val, str):
            flattened.append(val)
        elif isinstance(val, Iterable):
            for e in val:
                flattened.append(e)
        else:
            raise ValueError

    # Anti-Interning, so each Literal is unique
    class LiteralElem(Enum):
        ELEM = flattened
    literal = Literal[LiteralElem.ELEM]
    
    # Literal args get reassigned
    literal.__args__ = flattened

    return literal
