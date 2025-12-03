# https://adventofcode.com/2025/day/3


# Input

with open('2025/day-03-input.txt') as file:
    banks = tuple(tuple(map(int, stringbank.strip())) for stringbank in file.readlines())


# Solution

def maxjoltage(bank: str, n: int) -> int:
    '''Returns the maximum joltage by activating 'n' batteries from a bank.'''
    length = len(bank)

    total = 0
    start = 0
    for excluded in range(n - 1, -1, -1):
        searchrange = bank[start : length - excluded]
        maximum = max(searchrange)
        total = total * 10 + maximum
        start += searchrange.index(maximum) + 1

    return total


twobatteries = 0
twelvebatteries = 0
for bank in banks:
    twobatteries += maxjoltage(bank, n=2)
    twelvebatteries += maxjoltage(bank, n=12)

print('Silver solution:', twobatteries)
print('Gold solution:', twelvebatteries)
