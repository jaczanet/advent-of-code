# https://adventofcode.com/2025/day/2


from itertools import count


# Input

with open('2025/inputs/day-02.txt') as file:
    ranges = [
        (start, stop)
        for start, stop in (
            map(int, stringrange.split('-'))
            for stringrange in file.read().split(',')
        )
    ]


# Solution

ranges.sort()


MAXIMUM = ranges[-1][1]
candidates = set()

for repeat in range(2, len(str(MAXIMUM)) + 1):
    for pattern in map(str, count()):

        invalid = int(pattern * repeat)

        if invalid > MAXIMUM:
            break
        else:
            candidates.add(invalid)

candidates = sorted(candidates)


twice = 0
repeated = 0

stop = -float('Inf')
bounds = iter(ranges)

for id in candidates:
    while id > stop:
        start, stop = next(bounds)
    else:
        if id >= start:
            repeated += id

            string = str(id)
            mid = len(string) // 2
            if string[:mid] == string[mid:]:
                twice += id

print('Silver solution:', twice)
print('Gold solution:', repeated)
