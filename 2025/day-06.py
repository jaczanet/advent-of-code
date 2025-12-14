# https://adventofcode.com/2025/day/6


from operator import add, mul
from functools import reduce


# Constants

OPERATORS = {'+': add, '*': mul}


# Input

with open('2025/day-06-input.txt') as file:
    worksheet = map(str.split, file)
    problems = tuple(
        {
            'operation': OPERATORS[column[-1]],
            'numbers': tuple(map(int, column[:-1])),
        }
        for column in zip(*worksheet)
    )


cephalopodmath = list()
with open('2025/day-06-input.txt') as file:
    lines = file.read().strip().split('\n')

padding = max(len(line) for line in lines) + 1  # '+1' to add an empty column after the last problem
addpadding = lambda string: string.ljust(padding)
columns = zip(*map(addpadding, lines), strict=True)

numbers = list()
for column in columns:
    if not numbers:
        operation = column[-1]
    content = ''.join(column[:-1]).strip()
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

solve = lambda problem: reduce(problem['operation'], problem['numbers'])

print('Silver solution:', sum(map(solve, problems)))
print('Gold solution:', sum(map(solve, cephalopodmath)))
