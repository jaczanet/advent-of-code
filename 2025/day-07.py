# https://adventofcode.com/2025/day/7


# Input

with open('2025/day-07-input.txt') as file:
    start = next(file).strip()
    diagram = file.read().strip()


beam = int(start.replace('.', '0').replace('S', '1'), base=2)
manifold = tuple(
    int(scheme.replace('.', '0').replace('^', '1'), base=2)
    for scheme in diagram.split('\n')[1::2]
)


# Solution

bits = len(start)
quantum = [0] * bits
quantum[start.index("S")] = 1

splits = 0

for splitters in manifold:

    hits = beam & splitters
    new = (hits << 1) | (hits >> 1)  # left and right shift

    beam &= ~splitters  # keep untouched beams
    beam |= new  # add new splitted beams

    mask = bin(hits)[2:].rjust(bits)
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
