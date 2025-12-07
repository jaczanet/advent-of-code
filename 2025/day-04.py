# https://adventofcode.com/2025/day/4

from itertools import product


# Input

with open('2025/day-04-input.txt') as file:
    diagram = tuple(list(line.strip()) for line in file)


# Solution

cells = len(diagram)
iswithinbounds = lambda x, y: 0 <= x < cells and 0 <= y < cells


def neighbours(center) -> set:
    """Given a center position, returns a set of all the neighbouring positions in the diagram."""
    x, y = center
    positions = {
        pos
        for dx, dy in product(range(-1, 2), repeat=2)
        if iswithinbounds(*(pos := (x + dx, y + dy)))
    }
    positions.remove(center)
    return positions


def remove(diagram) -> int:
    """Edits the matrix *IN PLACE* and returns the amount of removed paper rools."""
    collecting = list()  # stores (x, y) positions of the removable paper rolls

    for x, y in product(range(cells), repeat=2):
        if diagram[x][y] == '@':
            position = (x, y)

            paperaround = [diagram[x][y] for x, y in neighbours(position)].count('@')

            if paperaround < 4:
                collecting.append(position)

    for x, y in collecting:
        diagram[x][y] = 'x'

    return len(collecting)


total = remove(diagram)
print('Silver solution:', total)

while collected := remove(diagram):
    total += collected
print('Gold solution:', total)
