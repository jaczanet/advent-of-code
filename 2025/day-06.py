# https://adventofcode.com/2025/day/6


from operator import add, mul
from functools import reduce


solve = lambda problem: reduce(problem['operation'], problem['numbers'])


# Constants

OPERATORS = {'+': add, '*': mul}


# Input

with open('2025/day-06-input.txt') as file:
    worksheet = map(str.split, file)
    problems = tuple(
        {
            'operation': OPERATORS[operation],
            'numbers': tuple(map(int, numbers)),
        }
        for *numbers, operation in zip(*worksheet)
    )


cephalopodmath = list()
with open('2025/day-06-input.txt') as file:
    lines = file.read().splitlines()

padding = max(len(line) for line in lines) + 1  # '+1' to add an empty column after the last problem
addpadding = lambda string: string.ljust(padding)
columns = zip(*map(addpadding, lines), strict=True)

numbers = list()
for *digits, operation_or_space in columns:
    if not numbers:
        operation = operation_or_space
    content = ''.join(digits).strip()
    if content:
        numbers.append(content)
    else:  # empty column found: delimiter for problem's end
        cephalopodmath.append(
            {
                'operation': OPERATORS[operation],
                'numbers': tuple(map(int, numbers)),
            }
        )
        numbers.clear()


# Solution

print('Silver solution:', sum(map(solve, problems)))
print('Gold solution:', sum(map(solve, cephalopodmath)))
