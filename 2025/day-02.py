# https://adventofcode.com/2025/day/2

# Input

with open('2025/day-02-input.txt') as file:
    instructions = file.read().strip()


ranges = []
for stringrange in instructions.split(','):
    start, stop = stringrange.split('-')
    ranges.append(range(int(start), int(stop) + 1))


# Solution

# def isvalid(id: int) -> bool:
#     string = str(id)
#     half = len(string) // 2
#     return string[:half] != string[half:]


def repeatedslice(string: str, slicelen: int) -> bool:
    """Check if a string is formed as a repeated slice of length 'slicelen'"""
    slices = (string[i : i + slicelen] for i in range(0, len(string), slicelen))
    return len(set(slices)) == 1


def istwice(id: int) -> bool:
    string = str(id)
    if (length := len(string)) % 2:  # when it's of odd length
        return False
    return repeatedslice(string, length // 2)


def isrepetition(id: int) -> bool:
    string = str(id)
    for slicelen in range(1, len(string) // 2 + 1):
        if repeatedslice(string, slicelen):
            return True


repeatedtwice = 0
atleasttwice = 0

for idrange in ranges:
    for id in idrange:

        if istwice(id):
            repeatedtwice += id

        if isrepetition(id):
            atleasttwice += id

print('Silver solution:', repeatedtwice)
print('Gold solution:', atleasttwice)
