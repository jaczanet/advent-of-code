# https://adventofcode.com/2025/day/2


from functools import cache


@cache  # prevent useless recalculation
def submultiples(n: int) -> tuple[int]:
    # tailored to the problem domain
    divisors = set()
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors.remove(n)
    return tuple(sorted(divisors, reverse=True))


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

        for slicelen in submultiples(length):  # in decreasing order
            if string == string[:slicelen] * (length // slicelen):

                repeated += id

                if 2 * slicelen == length:
                    twice += id

                break

print('Silver solution:', twice)
print('Gold solution:', repeated)
