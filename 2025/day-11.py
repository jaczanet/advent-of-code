# https://adventofcode.com/2025/day/11

from functools import partial


# Constants

start = 'you'  # starting device label
end = 'out'  # ending device label


# Input

with open('2025/day-11-input.txt') as file:
    devices = {
        device: outputs.strip().split()
        for device, outputs in map(partial(str.split, sep=':'), file)
    }


# Solution

paths = 0

stack = devices[start]
while stack:

    device = stack.pop()

    if device == end:
        paths += 1
    else:
        stack.extend(devices[device])


print('Silver solution:', paths)
