# https://adventofcode.com/2025/day/1


class Rotation(int):

    def __new__(cls, string, /):
        direction = string[0]
        clicks = string[1:]

        if direction == 'L':
            sign = -1
        elif direction == 'R':
            sign = +1
        else:
            raise ValueError(f"invalid literal for a LEFT-RIGTH Rotation(): '{string}'")

        instance = super().__new__(cls, sign * int(clicks))
        return instance

    def __str__(self, /) -> str:
        string = super().__str__()

        if self < 0:
            # remove the sign '-'
            string = string[1:]

        if self < 0:
            direction = 'L'
        elif self > 0:
            direction = 'R'

        return direction + string


# Constants

mod = 100
start = 50


# Input

with open('2025/day-01-input.txt') as instructions:
    rotations = [Rotation(line.strip()) for line in instructions]


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

result = print('Silver solution:', zerohits)
result = print('Gold solution:', zeropasses)
