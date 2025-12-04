# https://adventofcode.com/2025/day/4


# Input

with open('2025/day-04-input.txt') as file:
    diagram = [list(line.strip()) for line in file]


# Solution

from collections import namedtuple
from itertools import product
from itertools import starmap


Position = namedtuple('Position', ['x', 'y'])


cells = len(diagram)
iswithinbounds = lambda pos: 0 <= pos.x < cells and 0 <= pos.y < cells


def neighbours(center: Position) -> set[Position]:
    """Given a center position, returns a set of all the neighbouring positions in the diagram."""
    x, y = center
    positions = {
        pos
        for dx, dy in product(range(-1, 2), repeat=2)
        if iswithinbounds(pos := Position(x + dx, y + dy))
    }
    positions.remove(center)
    return positions


class Diagram(list):

    def __getitem__(self, index, /):
        if isinstance(index, tuple):
            return super().__getitem__(index[0])[index[1]]
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value, /):
        if isinstance(index, tuple):
            self[index[0]][index[1]] = value
        else:
            super().__setitem__(index, value)


diagram = Diagram(diagram)


def remove(diagram: Diagram) -> int:
    """Edits the matrix *IN PLACE* and returns the amount of removed paper rools."""
    count = 0
    collecting = set()

    for pos in starmap(Position, product(range(cells), repeat=2)):
        if (elem := diagram[pos]) == '.' or elem == 'x':
            continue

        paperaround = [diagram[neighpos] for neighpos in neighbours(pos)].count('@')
        if paperaround < 4:
            collecting.add(pos)
            count += 1

    for pos in collecting:
        diagram[pos] = 'x'

    return count


collected = 0
collected += remove(diagram)
print('Silver solution:', collected)

total = collected
while collected:
    collected = remove(diagram)
    total += collected

print('Gold solution:', total)
