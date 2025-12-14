# https://adventofcode.com/2025/day/7


from functools import partial


# Input

with open('2025/day-07-input.txt') as file:
    start = next(file)
    diagram = file.read()


beam = int(start.replace('.', '0').replace('S', '1'), base=2)
manifold = tuple(
    map(
        partial(int, base=2),
        diagram.replace('.', '0').replace('^', '1').splitlines()[1::2],
    )
)


# Solution

BITS = len(start.strip())

quantum = [0] * BITS
quantum[start.index("S")] = 1

splits = 0

for splitters in manifold:

    hits = beam & splitters
    new = (hits << 1) | (hits >> 1)  # left and right shift

    beam &= ~splitters  # keep untouched beams
    beam |= new  # add new splitted beams

    mask = bin(hits)[2:].rjust(BITS, '0')
    for i, bit in enumerate(mask):
        if bit == '1':

            t = quantum[i]
            quantum[i - 1] += t
            quantum[i + 1] += t
            quantum[i] = 0

            splits += 1

timelines = sum(quantum)

print('Silver solution:', splits)
print('Gold solution:', timelines)
