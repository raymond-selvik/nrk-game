from enum import Enum
from typing import Self


class FieldType(Enum):
    GREEN = 'G'
    BLUE = 'B'
    PINK = 'P'
    ORANGE = 'O'
    EMPTY = 'X'

    def parse(str) -> Self:
        if str == 'G': return FieldType.GREEN
        elif str == 'B': return FieldType.BLUE
        elif str == 'P': return FieldType.PINK
        elif str == 'O': return FieldType.ORANGE
        else: return None