# https://adventofcode.com/2025/day/9


from csv import reader as csvreader
from collections import namedtuple
from itertools import combinations


Position = namedtuple('Position', ['x', 'y'])


# Input

with open('2025/inputs/day-09.txt') as file:
    redtiles = tuple(Position(*map(int, coords)) for coords in csvreader(file))


# Solution

area = lambda p, q: abs((p.x - q.x + 1) * (p.y - q.y + 1))  # rectangle area enclosed between two tiles

print('Silver solution:', max(area(a, b) for a, b in combinations(redtiles, 2)))
