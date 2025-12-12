# https://adventofcode.com/2025/day/4

from collections import namedtuple
from itertools import starmap, product
from functools import cache

Coordinate = namedtuple('Coordinate', ['i', 'j'])


# Input

with open('2025/day-04-input.txt') as file:
    diagram = tuple(list(line.strip()) for line in file)


# Solution

limit = len(diagram)

iswithinbounds = lambda coord: 0 <= coord.i < limit and 0 <= coord.j < limit

allcoords = tuple(starmap(Coordinate, product(range(limit), repeat=2)))


contourdeltas = set(product(range(-1, 2), repeat=2))
contourdeltas.remove((0, 0))

contour = lambda coord: (Coordinate(coord.i + dy, coord.j + dx) for dy, dx in contourdeltas)

neighbours = lambda coord: tuple(filter(iswithinbounds, contour(coord)))
neighbours = cache(neighbours)


ispaperroll = lambda coord: diagram[coord.i][coord.j] == '@'

paperaround = lambda coord: len(tuple(filter(ispaperroll, neighbours(coord))))

iscollectable = lambda coord: paperaround(coord) < 4


def remove() -> int:
    """Edits the matrix *IN PLACE* and yields the amount of removed paper rools."""
    papercoords = set(filter(ispaperroll, allcoords))
    while collectable := set(filter(iscollectable, papercoords)):

        for coord in collectable:
            diagram[coord.i][coord.j] = 'x'
        else:
            papercoords -= collectable

        yield len(collectable)


collector = remove()
collected = next(collector)

print('Silver solution:', collected)
print('Gold solution:', collected + sum(collector))
