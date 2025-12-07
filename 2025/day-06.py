# https://adventofcode.com/2025/day/6

from operator import add, mul

# Input

with open('2025/day-06-input.txt') as file:
    worksheet = map(str.split, file)
    problems = [
        {
            'operation': {'+': add, '*': mul}[column[-1]],
            'numbers': tuple(map(int, column[:-1])),
        }
        for column in zip(*worksheet)
    ]


# Solution


sumproblems = 0
for problem in problems:

    operation = problem['operation']
    identity = {add: 0, mul: 1}
    result = identity[operation]

    for number in problem['numbers']:
        result = operation(result, number)

    sumproblems += result

print('Silver solution:', sumproblems)
