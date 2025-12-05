# https://adventofcode.com/2025/day/5


# Input

with open('2025/day-05-input.txt') as file:
    ranges, ids = file.read().strip().split('\n\n')

freshranges = tuple(
    range(start, stop + 1)
    for start, stop in (
        map(int, stringrange.split('-'))
        for stringrange in ranges.split('\n')
    )
)

inventory = tuple(map(int, ids.split('\n')))


# Solution

count = 0
for id in inventory:
    for idrange in freshranges:
        if id in idrange:
            count += 1
            break

print('Silver solution:', count)
