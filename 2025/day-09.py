# https://adventofcode.com/2025/day/9


from csv import reader as csvreader
from collections import namedtuple
from itertools import combinations, pairwise
from functools import partial


Position = namedtuple('Position', ['x', 'y'])


# Input

with open('2025/inputs/day-09.txt') as file:
    redtiles = tuple(Position(*map(int, coords)) for coords in csvreader(file))


# Solution

# rectangle area enclosed between two tiles
area = lambda p, q: (abs(p.x - q.x) + 1) * (abs(p.y - q.y) + 1)

# red tiles pairs sorter in decreasing order according to their enclosed area
pairs = sorted(
    combinations(redtiles, 2),
    key=lambda tiles: area(tiles[0], tiles[1]),
    reverse=True,
)

a, b = pairs[0]
print('Silver solution:', area(a, b))

contour = tuple(pairwise(redtiles + (redtiles[0],)))

horizontal = list()
vertical = list()

for edge in contour:
    p, q = edge

    if p.x == q.x:
        vertical.append(sorted(edge))
    elif p.y == q.y:
        horizontal.append(sorted(edge))
    else:
        raise ValueError


def valid(pair: tuple[Position]) -> bool:
    xs = sorted(tile.x for tile in pair)
    ys = sorted(tile.y for tile in pair)

    # see if any of the sides intersect the contour
    # check if the horizontal sides intersect any vertical edge of the contour
    # and if the vertical sides intersect any horizontal edges of the contour

    #        c
    #     -------
    #   d |     | b
    #     -------
    #        a

    for edge in horizontal:
        p, q = edge

        if p.x <= xs[0] <= q.x:  # side d might cross edge
            if ys[0] < p.y < ys[1]:
                return False

        if p.x <= xs[1] <= q.x:  # side b might cross edge
            if ys[0] < p.y < ys[1]:
                return False

    for edge in vertical:
        p, q = edge

        if p.y <= ys[0] <= q.y:  # side a might cross edge
            if xs[0] < p.x < xs[1]:
                return False

        if p.y <= ys[1] <= q.y:  # side b might cross edge
            if xs[0] < p.x < xs[1]:
                return False

    return True


a, b = next(filter(valid, pairs))
print('Gold solution:', area(a, b))
