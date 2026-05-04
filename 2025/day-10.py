# https://adventofcode.com/2025/day/10


import numpy as np
from scipy.optimize import milp


# Constants

INDICATORS = {'.': 0, '#': 1}


# Input

problems = list()
with open('2025/inputs/day-10.txt') as file:
    for lights, *buttons, _ in map(str.split, file.readlines()):

        b = np.fromiter(map(INDICATORS.__getitem__, lights.strip('[]')), dtype=bool)

        A = np.zeros((len(b), len(buttons)), dtype=bool)
        for j, string in enumerate(buttons):
            idxs = tuple(map(int, string.strip('()').split(',')))
            A[idxs, j] = True

        problems.append((A, b))


# Solution

# Integer linear programming optimization problem
# minimise: sum(x)
# subject to: (A @ x) % 2 = b
# turn constraints into standard form with the introduction of slack variables k
# <=> A @ x -2k = b

presses = 0
for A, b in problems:

    n, m = A.shape

    c = np.r_[np.ones(m), np.zeros(n)]

    M = np.c_[A, -2 * np.eye(n)]

    presses += milp(c, constraints=(M, b, b), integrality=1).fun

print('Silver solution:', int(presses))
