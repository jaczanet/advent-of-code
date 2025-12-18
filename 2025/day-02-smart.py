# https://adventofcode.com/2025/day/2


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


maximum = ranges[-1][1]
maxdigits = len(str(maximum))

generated = set()

for digits in range(1, maxdigits // 2 + 1):
    magnitude = 10**digits

    for repeat in range(2, maxdigits // digits + 1):
        mask = (magnitude**repeat - 1) // (magnitude - 1)

        for pattern in range(
            magnitude // 10,
            min(magnitude, maximum // mask + 1),
        ):
            generated.add(pattern * mask)


candidates = sorted(generated)


reptwice = 0
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
                reptwice += id

print('Silver solution:', reptwice)
print('Gold solution:', repeated)
