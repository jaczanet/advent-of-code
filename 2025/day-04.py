# https://adventofcode.com/2025/day/4


from collections import namedtuple
from itertools import starmap, product
from functools import cache


Coordinate = namedtuple('Coordinate', ['i', 'j'])


# Constants

PAPER_STRING = '@'


# Input

with open('2025/day-04-input.txt') as file:
    diagram = tuple(list(line.strip()) for line in file)


# Solution

LIMIT = len(diagram)

iswithinbounds = lambda coord: 0 <= coord.i < LIMIT and 0 <= coord.j < LIMIT

ALLCOORDS = tuple(starmap(Coordinate, product(range(LIMIT), repeat=2)))


contourdeltas = set(product(range(-1, 2), repeat=2))
contourdeltas.remove((0, 0))
CONTOURDELTAS = frozenset(contourdeltas)
del contourdeltas

contour = lambda coord: (Coordinate(coord.i + dy, coord.j + dx) for dy, dx in CONTOURDELTAS)

neighbours = lambda coord: tuple(filter(iswithinbounds, contour(coord)))
neighbours = cache(neighbours)


ispaper = lambda coord: diagram[coord.i][coord.j] == PAPER_STRING

paperaround = lambda coord: len(tuple(filter(ispaperroll, neighbours(coord))))

iscollectable = lambda coord: paperaround(coord) < 4


def remove() -> int:
    """Edits the matrix *IN PLACE* and yields the amount of removed paper rools."""
    papercoords = set(filter(ispaper, ALLCOORDS))
    while collectables := set(filter(iscollectable, papercoords)):

        for coord in collectables:
            diagram[coord.i][coord.j] = 'x'
        else:
            papercoords -= collectables

        yield len(collectables)


collector = remove()
collected = next(collector)

print('Silver solution:', collected)
print('Gold solution:', collected + sum(collector))
