# https://adventofcode.com/2025/day/8

from csv import reader as csvreader
from collections import namedtuple, Counter
from itertools import combinations
from math import sqrt, prod


Position = namedtuple('Position', ['x', 'y', 'z'])
Connection = namedtuple('Connection', ['i', 'j', 'distance'])


# Constants

# for silver part
n = 1000  # total number of connections to perform
m = 3  # number of largest circuits to be considered


# Input

with open('2025/day-08-input.txt') as file:
    jboxs = tuple(Position(*map(int, coords)) for coords in csvreader(file))


# Solution

euclideandistance = lambda p, q: sqrt(sum((pcoord - qcoord) ** 2 for pcoord, qcoord in zip(p, q, strict=True)))

edges = [
    Connection(i, j, euclideandistance(jboxs[i], jboxs[j]))
    for i, j in combinations(range(len(jboxs)), 2)
    if i != j
]
edges.sort(key=lambda connection: connection.distance)

parent = list(range(len(jboxs)))  # track the root jbox for every circuit

connections = 0
# perform connections until only one circuit (disjoint set) remains
for i, j, distance in edges:
    u = parent[i]
    v = parent[j]
    # substitute the root of j with the root of i
    for idx, p in enumerate(parent):
        if p == v:
            parent[idx] = u

    connections += 1

    if connections == n:
        circuits = Counter(parent)
        print('Silver solution:', prod(size for root, size in circuits.most_common(m)))

    if all(p == u for p in parent):
        print('Gold solution:', jboxs[i].x * jboxs[j].x)
        break
