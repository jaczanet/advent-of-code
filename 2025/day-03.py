# https://adventofcode.com/2025/day/3


def maxjoltage(bank: tuple[int], n: int) -> int:
    """Returns the maximum joltage obtainable by activating n batteries in a bank."""
    total = 0

    start = 0
    end = len(bank) - n + 1
    for i in range(n):
        searchrange = bank[start : end + i]

        maximum = max(searchrange)
        total = total * 10 + maximum

        start += searchrange.index(maximum) + 1

    return total


# Input

with open('2025/inputs/day-03.txt') as file:
    banks = tuple(tuple(map(int, stringbank.strip())) for stringbank in file)


# Solution

twobatteries = 0
twelvebatteries = 0

for bank in banks:
    twobatteries += maxjoltage(bank, n=2)
    twelvebatteries += maxjoltage(bank, n=12)

print('Silver solution:', twobatteries)
print('Gold solution:', twelvebatteries)
