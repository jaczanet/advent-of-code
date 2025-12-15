# https://adventofcode.com/2025/day/2


from functools import cache


def divisors(n: int) -> set[int]:
    divisors = {1, n}
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


@cache
def submultiples(n: int) -> set[int]:
    submultiples = divisors(n)
    submultiples.remove(n)
    return submultiples


# Input

with open('2025/inputs/day-02.txt') as file:
    ranges = tuple(
        range(start, stop + 1)
        for start, stop in (
            map(int, stringrange.split('-'))
            for stringrange in file.read().split(',')
        )
    )


# Solution

twice = 0
repeated = 0

for idrange in ranges:
    for id in idrange:

        string = str(id)
        length = len(string)

        for slicelen in sorted(submultiples(length), reverse=True):
            slices = (string[i : i + slicelen] for i in range(0, length, slicelen))

            pattern = next(slices)
            if all(slc == pattern for slc in slices):

                repeated += id

                if 2 * slicelen == length:
                    twice += id

                break

print('Silver solution:', twice)
print('Gold solution:', repeated)
