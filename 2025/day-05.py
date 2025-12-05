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

# remove redundancy
uniques = list()
freshranges = sorted(freshranges, key=lambda r: (r.start, r.stop))
prevstart = prevstop = -1

for idrange in freshranges:
    currstart, currstop = idrange.start, idrange.stop

    # merge
    if currstart <= prevstop:
        prevstop = max(prevstop, currstop)

    else:
        uniques.append(range(prevstart, prevstop))
        prevstart, prevstop = currstart, currstop
else:
    # handle the final case
    uniques.append(range(prevstart, prevstop))

freshranges = uniques

inventory = sorted(inventory)

fresh = 0
last = 0
for id in inventory:
    for j in range(last, len(freshranges)):
        idrange = freshranges[j]
        if id < idrange.start:
            break
        elif id in idrange:
            fresh += 1
            last = j
            break
        elif id >= idrange.stop:
            last = j


print('Silver solution:', fresh)


total = 0
for idrange in freshranges:
    total += len(idrange)

print('Gold solution:', total)
