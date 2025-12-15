# https://adventofcode.com/2025/day/5


# Input

with open('2025/inputs/day-05.txt') as file:
    intervals, ids = file.read().split('\n\n')

freshranges = [
    (start, stop)
    for start, stop in (
        map(int, stringrange.split('-'))
        for stringrange in intervals.splitlines()
    )
]

inventory = list(map(int, ids.splitlines()))


# Solution

freshranges.sort()
inventory.sort()


mergedranges = list()
mutableranges = map(list, freshranges)

prev = next(mutableranges)
mergedranges.append(prev)

for curr in mutableranges:

    # prev: [a, b]; curr, at most: [b + 1, x] -> merge
    if curr[0] <= prev[1] + 1:

        # update the previous range's stop *in place*
        prev[1] = max(prev[1], curr[1])

    else:
        mergedranges.append(curr)
        prev = curr


fresh = 0
total = 0

stop = -float('Inf')
ranges = iter(mergedranges)

try:

    for id in inventory:
        while id > stop:
            start, stop = next(ranges)
            total += -start + stop + 1
        else:
            if id >= start:
                fresh += 1

except StopIteration:
    pass

print('Silver solution:', fresh)
print('Gold solution:', total)
