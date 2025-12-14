# https://adventofcode.com/2025/day/8


from csv import reader as csvreader
from collections import namedtuple
from itertools import combinations
from heapq import heapify, heappop, nlargest
from math import prod


Position = namedtuple('Position', ['x', 'y', 'z'])


class UnionFind:

    __slots__ = '_disjoint', '_parents', '_sizes'

    def __init__(self, n: int):
        self._disjoint = n
        self._parents = list(range(n))
        self._sizes = [1] * n

    @property
    def disjoint(self, /) -> int:
        return self._disjoint

    @property
    def sizes(self, /):
        return iter(self._sizes)

    def find(self, key: int, /):
        if self._parents[key] != key:
            self._parents[key] = self.find(self._parents[key])  # path compression

        return self._parents[key]

    def union(self, v: int, u: int, /):
        if (vroot := self.find(v)) != (uroot := self.find(u)):

            self._disjoint -= 1

            # Union by size: attach the smaller tree under the root of
            # the larger tree to keep the tree as flat as possible.

            if self._sizes[bigger := vroot] < self._sizes[smaller := uroot]:
                bigger, smaller = smaller, bigger

            self._parents[smaller] = bigger
            self._sizes[bigger] += self._sizes[smaller]


# Constants

N = 1000  # total number of connections to perform, for silver solution
M = 3  # number of largest circuits to consider, for silver solution


# Input

with open('2025/day-08-input.txt') as file:
    jboxs = tuple(Position(*map(int, coords)) for coords in csvreader(file))


# Solution

norm = lambda p, q: ((p.x - q.x) ** 2 + (p.y - q.y) ** 2 + (p.z - q.z) ** 2)

edges = [(norm(jboxs[i], jboxs[j]), i, j) for i, j in combinations(range(len(jboxs)), 2)]

connections = 0

circuits = UnionFind(n=len(jboxs))

heapify(edges)
while edges:
    distance, i, j = heappop(edges)

    circuits.union(i, j)

    connections += 1

    if connections == N:
        print('Silver solution:', prod(nlargest(M, circuits.sizes)))

    if circuits.disjoint == 1:
        print('Gold solution:', jboxs[i].x * jboxs[j].x)
        break
