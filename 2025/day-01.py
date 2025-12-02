# https://adventofcode.com/2025/day/1


# Constants

mod = 100
start = 50


# Input

def asintger(rotation: str) -> int:
    direction = rotation[0]
    clicks = rotation[1:]

    if direction == 'L':
        sign = -1
    elif direction == 'R':
        sign = +1

    return sign * int(clicks)


with open('2025/day-01-input.txt') as instructions:
    rotations = tuple(map(asintger, instructions))


# Solution

zerohits = 0  # count how many times the dial is left pointing at '0' after a rotation
zeropasses = 0  # count how many times the dial points to '0' during or after a rotation

position = start
for rotation in rotations:
    if position == 0 and rotation < 0:
        zeropasses -= 1

    position += rotation

    zeropasses += int(abs(position - mod / 2) + mod / 2) // mod

    position %= mod

    zerohits += position == 0

print('Silver solution:', zerohits)
print('Gold solution:', zeropasses)
