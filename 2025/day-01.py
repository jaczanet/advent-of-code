# https://adventofcode.com/2025/day/1


def asintger(rotation: str) -> int:
    direction = rotation[0]
    clicks = rotation[1:]

    if direction == 'L':
        sign = -1
    elif direction == 'R':
        sign = +1

    return sign * int(clicks)


# Constants

MOD = 100
START = 50


# Input

with open('2025/day-01-input.txt') as file:
    rotations = tuple(map(asintger, file))


# Solution

zerohits = 0  # count how many times the dial is left pointing at '0' after a rotation
zeropasses = 0  # count how many times the dial points to '0' during or after a rotation

position = START
for rotation in rotations:
    if -rotation >= position and position != 0:
        zeropasses += 1

    position += rotation

    zeropasses += abs(position) // MOD

    position %= MOD

    zerohits += position == 0

print('Silver solution:', zerohits)
print('Gold solution:', zeropasses)
