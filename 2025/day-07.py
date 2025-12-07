# https://adventofcode.com/2025/day/7

from enum import Enum
from functools import partial, cache


# Input

with open('2025/day-07-input.txt') as file:
    start = next(file).strip()
    diagram = file.read().strip()


beam = int('0b' + start.replace('.', '0').replace('S', '1'), base=2)
manifold = tuple(
    int('0b' + scheme.replace('.', '0').replace('^', '1'), base=2)
    for scheme in diagram.split('\n')[1::2]
)


# Solution


class Direction(Enum):
    LEFT = -1
    RIGHT = 1


def traverse(beam: int, splitters: int, direction: Direction) -> int:
    """Returns the beam after crossing the row of splitters, moving in the specified direction."""

    hits = beam & splitters

    match direction:
        case Direction.LEFT:
            new = hits << 1
        case Direction.RIGHT:
            new = hits >> 1
        case _:
            raise ValueError("direction must be Direction.LEFT or Direction.RIGHT")

    beam &= ~splitters  # keep untouched beams
    beam |= new  # add new split beams

    return beam


def splits(beam: int, manifold) -> int:
    """Returns the total number of times a tachyon beam is split in a manifold."""
    splits = 0
    for splitters in manifold:

        splits += bin(beam & splitters).count('1')  # count of hits

        # combined new beam after crossing the row of splitters
        left = traverse(beam, splitters, Direction.LEFT)
        right = traverse(beam, splitters, Direction.RIGHT)
        beam = left | right

    return splits


def timelines(beam, manifold) -> int:
    """Returns the number of different timelines a beam traversing the manifold may end up in."""

    n = len(manifold)

    @cache
    def _timelines(ray, level):
        # end of backtracking
        if level == n:
            return 1

        left = traverse(ray, manifold[level], Direction.LEFT)
        right = traverse(ray, manifold[level], Direction.RIGHT)

        uniquerays = set((left, right))

        return sum(map(partial(_timelines, level=level + 1), uniquerays))

    return _timelines(beam, level=0)


print('Silver solution:', splits(beam, manifold))
print('Gold solution:', timelines(beam, manifold))
