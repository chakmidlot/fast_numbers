from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Level:
    length: int
    delay: float


LEVELS = [
    Level(4, 0.8),
    Level(5, 0.6),
    Level(6, 0.5),
    Level(6, 0.4),
    Level(6, 0.3),
    Level(7, 0.5),
    Level(7, 0.4),
    Level(8, 0.7),
    Level(8, 0.6),
    Level(8, 0.5),
    Level(8, 0.4),
    Level(9, 0.7),
    Level(9, 0.6),
    Level(9, 0.5),
]
