# https://adventofcode.com/2025/day/11


from collections import deque
from functools import cached_property, partial
from itertools import chain, pairwise, starmap
from math import prod


class Graph:

    def __init__(self, /, adjencylist):
        self._adjlist = adjencylist.copy()  # prevent external modifications

        for missing in set(chain(*adjencylist.values())) - set(adjencylist):
            self._adjlist[missing] = tuple()  # reduce edge cases

    # Graph doesn't provide an API to insert new edges, thus it can't be
    # modified after initialisation. Hence, its properties can be cached.

    @cached_property
    def vertices(self, /) -> frozenset:
        return frozenset(self._adjlist.keys())

    def edgesof(self, *vertices):
        for u in vertices:
            for v in self._adjlist[u]:
                yield (u, v)

    @cached_property
    def edges(self, /) -> tuple:
        return tuple(self.edgesof(*self.vertices))

    @cached_property
    def indegrees(self, /) -> dict:
        """Return a mapping from each vertex to its in-degree value."""
        indegree = dict.fromkeys(self.vertices, 0)

        for u, v in self.edges:
            indegree[v] += 1

        return indegree

    @cached_property
    def ordtopological(self, /) -> tuple:
        """Return a sequence with the vertices in topological order."""

        indegree = dict(self.indegrees)  # mutable copy
        queue = deque(filter(lambda v: indegree[v] == 0, self.vertices))
        toposort = list()

        while queue:

            vertex = queue.popleft()
            toposort.append(vertex)

            # Once a vertex is placed in the topological order,
            # "remove" its edges from the graph: i.e. decrease the
            # in-degree value of the connected nodes.

            for _, node in self.edgesof(vertex):
                indegree[node] -= 1

                # A vertex can be insierted in the topological order
                # once all edges directed into the vertex have been
                # "removed": i.e. its in-degree value has become 0.

                if indegree[node] == 0:
                    queue.append(node)

        return tuple(toposort)

    @cached_property  # precompute O(V) and cache for O(1) acces (used in Graph.paths)
    def _index(self, /) -> dict:
        """Return a mapping from each vertex to its index in the topological order."""
        return {vertex: idx for idx, vertex in enumerate(self.ordtopological)}

    def paths(self, /, start, end) -> int:
        """Computes the toal number of possible paths from 'start' to 'end'."""
        countpaths = dict.fromkeys(self.vertices, 0)
        countpaths[start] = 1  # base case

        reachables = self.ordtopological[self._index[start] : self._index[end]]

        for u, v in self.edgesof(*reachables):
            countpaths[v] += countpaths[u]

        return countpaths[end]


# Constants

YOU = 'you'  # starting device label
OUT = 'out'  # ending device label
SERVER = 'svr'  # server device label
DAC = 'dac'  # dac device label
FFT = 'fft'  # fft device label


# Input

with open('2025/day-11-input.txt') as file:
    network = Graph(
        {
            device: tuple(outputs.split())
            for device, outputs in map(partial(str.split, sep=':'), file)
        }
    )


# Solution

print('Silver solution:', network.paths(start=YOU, end=OUT))
print('Gold solution:', prod(starmap(network.paths, pairwise((SERVER, FFT, DAC, OUT)))))
