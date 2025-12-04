# https://adventofcode.com/2025/day/4

from itertools import product


class Matrix(list):
    # Essentially a list of lists that enables indexing using tuples
    # e.g. matrix[(x, y)]
    # e.g. matrix[x, y]
    # which are equivalent to matrix[x][y]

    def __getitem__(self, index, /):
        if isinstance(index, tuple):
            if len(index) > 2:
                raise ValueError("Index must be a tuple of exactly two elements (for 2D indexing).")
            return super().__getitem__(index[0])[index[1]]
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value, /):
        if isinstance(index, tuple):
            if len(index) > 2:
                raise ValueError("Index must be a tuple of exactly two elements (for 2D indexing).")
            self[index[0]][index[1]] = value
        else:
            super().__setitem__(index, value)


Position = tuple[int]


# Input

with open('2025/day-04-input.txt') as file:
    diagram = Matrix(list(line.strip()) for line in file)


# Solution

cells = len(diagram)
iswithinbounds = lambda x, y: 0 <= x < cells and 0 <= y < cells


def neighbours(center: Position) -> set[Position]:
    """Given a center position, returns a set of all the neighbouring positions in the diagram."""
    x, y = center
    positions = {
        pos
        for dx, dy in product(range(-1, 2), repeat=2)
        if iswithinbounds(*(pos := (x + dx, y + dy)))
    }
    positions.remove(center)
    return positions


def remove(diagram: Matrix) -> int:
    """Edits the matrix *IN PLACE* and returns the amount of removed paper rools."""
    collecting: set[Position] = set()

    for pos in product(range(cells), repeat=2):
        if diagram[pos] == '@':

            paperaround = [diagram[neighpos] for neighpos in neighbours(pos)].count('@')

            if paperaround < 4:
                collecting.add(pos)

    for pos in collecting:
        diagram[pos] = 'x'

    return len(collecting)


total = remove(diagram)
print('Silver solution:', total)

while collected := remove(diagram):
    total += collected
print('Gold solution:', total)
