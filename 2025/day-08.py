# https://adventofcode.com/2025/day/8

from collections import namedtuple, Counter
from math import sqrt, prod


Point = namedtuple('Point', ['x', 'y', 'z'])
Connection = namedtuple('Connection', ['i', 'j', 'distance'])


# Constants

n = 1000  # total number of connections to perform
m = 3  # total number of largest circuits to be considered


# Input

with open('2025/day-08-input.txt') as file:
    jboxs = tuple(Point(*map(int, coords.split(','))) for coords in file.read().strip().split('\n'))


# Solution

euclideandistance = lambda p, q: sqrt(sum((pcoord - qcoord) ** 2 for pcoord, qcoord in zip(p, q, strict=True)))

adjacencymatrix = tuple(tuple(euclideandistance(p, q) for q in jboxs) for p in jboxs)

edges = [
    Connection(i, j, distance)
    for i, row in enumerate(adjacencymatrix)
    for j, distance in enumerate(row[i:], start=i)
    if distance
]
edges.sort(key=lambda connection: connection.distance)

parent = list(range(len(jboxs)))  # track the root jbox for every circuit

# perform connection for first n (shortest) edges
for i, j, distance in edges[:n]:
    i = parent[i]
    j = parent[j]
    # substitute the root of j with the root of i
    for idx, p in enumerate(parent):
        if p == j:
            parent[idx] = i

circuits = Counter(parent)

print('Silver solution:', prod(size for root, size in circuits.most_common(m)))
