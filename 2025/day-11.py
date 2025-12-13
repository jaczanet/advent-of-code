# https://adventofcode.com/2025/day/11

from functools import partial


# Constants

YOU = 'you'  # starting device label
OUT = 'out'  # ending device label
SERVER = 'svr'  # server device label
DAC = 'dac'  # dac device label
FFT = 'fft'  # fft device label


# Input

with open('2025/day-11-input.txt') as file:
    connections = {
        device: tuple(outputs.strip().split())
        for device, outputs in map(partial(str.split, sep=':'), file)
    }

connections[OUT] = tuple()  # reduce edge cases


# Solution

def countpaths(start, end) -> int:
    memo = {end: 1}  # number of distinct paths from each node to the end

    def find(current):
        if current not in memo:
            memo[current] = sum(map(find, connections[current]))
        return memo[current]

    return find(start)


print('Silver solution:', countpaths(YOU, OUT))
print('Gold solution:', countpaths(SERVER, FFT) * countpaths(FFT, DAC) * countpaths(DAC, OUT))
