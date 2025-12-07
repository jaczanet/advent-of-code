# https://adventofcode.com/2025/day/7


# Input

with open('2025/day-07-input.txt') as file:
    start = next(file).strip()
    manifold = file.read().strip()


beam = int('0b' + start.replace('.', '0').replace('S', '1'), base=2)
splitters = [
    int('0b' + scheme.replace('.', '0').replace('^', '1'), base=2)
    for scheme in manifold.split('\n')[1::2]
]

# Solution

splits = 0
for row in splitters:

    hits = beam & row
    new = (hits << 1) | (hits >> 1)  # left and right shift

    beam &= ~row  # keep untouched beams
    beam |= new  # add new splitted beams

    splits += bin(hits).count('1')


print('Silver solution:', splits)
