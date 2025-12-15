# https://adventofcode.com/2025/day/12


from functools import partial
from math import prod


# Constants

MAXSIZE = 3 * 3


# Input

with open('2025/inputs/day-12.txt') as file:
    *shapes, layouts = file.read().split('\n\n')

sizes = tuple(string.count('#') for string in shapes)

regions = tuple(
    (prod(map(int, widthXlength.split('x'))), tuple(map(int, gifts.split())))
    for widthXlength, gifts in map(partial(str.split, sep=':'), layouts.splitlines())
)


# Solution

fits = 0

for area, quantities in regions:

    # lower bound: minimum required area
    # upper bound: maximum required area

    lowerbound = sum(map(prod, zip(quantities, sizes)))
    upperbound = sum(quantity * MAXSIZE for quantity in quantities)

    # can't fit
    if area < lowerbound:
        pass

    # could fit
    elif lowerbound <= area < upperbound:
        # No such cases in the puzzle input!
        raise NotImplementedError

    # fit for sure
    elif upperbound <= area:
        fits += 1

print('Solution:', fits)
