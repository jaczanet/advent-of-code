# https://adventofcode.com/2025/day/11


from functools import partial


def countpaths(graph, start, end) -> int:
    # 'graph' is expected to be the adjency list: for each vertex v,
    # graph[v] access the list of vertices reachable from v.

    memo = {end: 1}  # number of distinct paths from each vertex to the end

    def findpaths(vertex) -> int:
        if vertex not in memo:
            memo[vertex] = sum(map(findpaths, graph[vertex]))
        return memo[vertex]

    return findpaths(start)


# Constants

YOU = 'you'  # starting device label
OUT = 'out'  # ending device label
SERVER = 'svr'  # server device label
DAC = 'dac'  # dac device label
FFT = 'fft'  # fft device label


# Input

with open('2025/inputs/day-11.txt') as file:
    network = {
        device: tuple(outputs.split())
        for device, outputs in map(partial(str.split, sep=':'), file)
    }

network[OUT] = tuple()  # reduce edge cases


# Solution

connections = partial(countpaths, network)

print('Silver solution:', connections(YOU, OUT))
print('Gold solution:', connections(SERVER, FFT) * connections(FFT, DAC) * connections(DAC, OUT))
