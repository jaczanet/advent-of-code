# https://adventofcode.com/2025/day/9


from csv import reader as csvreader
from itertools import combinations, pairwise


def ordercoords(corners) -> tuple:
    (x1, y1), (x2, y2) = corners

    if y1 > y2:
        y1, y2 = y2, y1

    if x1 > x2:
        x1, x2 = x2, x1

    return x1, x2, y1, y2


def area(rectangle) -> int:
    xleft, xright, ytop, ylow = rectangle
    return (xright - xleft + 1) * (ylow - ytop + 1)


# Input

with open('2025/inputs/day-09.txt') as file:
    redtiles = tuple(tuple(map(int, coords)) for coords in csvreader(file))


# Solution

rectangles = sorted(
    map(ordercoords, combinations(redtiles, 2)),
    key=area,
    reverse=True,
)

horizontals = list()
verticals = list()

contour = pairwise(redtiles + (redtiles[0],))
for edge in map(ordercoords, contour):
    x1, x2, y1, y2 = edge

    if x1 == x2:
        verticals.append(edge)
    elif y1 == y2:
        horizontals.append(edge)


def valid(rectangle) -> bool:
    xleft, xright, ytop, ylow = rectangle

    # See if any of the rectangle sides intersect the contour: check if
    # the horizontal sides cross any vertical edge of the contour, or
    # if the vertical sides cross any horizontal edges of the contour.

    for x1, x2, _, y in horizontals:
        if (ytop < y < ylow) and (x1 <= xleft <= x2 or x1 <= xright <= x2):
            return False

    for x, _, y1, y2 in verticals:
        if (xleft < x < xright) and (y1 <= ytop <= y2 or y1 <= ylow <= y2):
            return False

    return True


print('Silver solution:', area(rectangles[0]))
print('Gold solution:', area(next(filter(valid, rectangles))))
