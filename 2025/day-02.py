# https://adventofcode.com/2025/day/2


# Input

with open('2025/day-02-input.txt') as file:
    ranges = tuple(
        range(start, stop + 1)
        for start, stop in (
            map(int, stringrange.split('-'))
            for stringrange in file.read().split(',')
        )
    )


# Solution

def submultiples(n: int) -> set[int]:
    submultiples = set()
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            submultiples.add(i)
            submultiples.add(n // i)
    submultiples.remove(n)
    return submultiples


twice = 0
repeated = 0

for idrange in ranges:
    for id in idrange:

        string = str(id)
        length = len(string)

        for slicelen in sorted(submultiples(length), reverse=True):
            slices = (string[i : i + slicelen] for i in range(0, length, slicelen))

            pattern = next(slices)
            for slice in slices:

                if slice != pattern:
                    break

            else:
                repeated += id

                if length == slicelen * 2:
                    twice += id

                break

print('Silver solution:', twice)
print('Gold solution:', repeated)
