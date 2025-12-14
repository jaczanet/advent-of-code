# https://adventofcode.com/2025/day/11


from functools import partial


def countpaths(graph, start, end) -> int:
    # 'graph' is expected to be the adjency list: for each vertex v,
    # graph[v] access the list of vertices reachable from v.

    memo = {end: 1}  # number of distinct paths from each vertex to the end

    def find(vertex):
        if vertex not in memo:
            memo[vertex] = sum(map(find, graph[vertex]))
        return memo[vertex]

    return find(start)


# Constants

YOU = 'you'  # starting device label
OUT = 'out'  # ending device label
SERVER = 'svr'  # server device label
DAC = 'dac'  # dac device label
FFT = 'fft'  # fft device label


# Input

with open('2025/day-11-input.txt') as file:
    network = {
        device: tuple(outputs.split())
        for device, outputs in map(partial(str.split, sep=':'), file)
    }

network[OUT] = tuple()  # reduce edge cases


# Solution

connections = partial(countpaths, network)

print('Silver solution:', connections(YOU, OUT))
print('Gold solution:', connections(SERVER, FFT) * connections(FFT, DAC) * connections(DAC, OUT))
