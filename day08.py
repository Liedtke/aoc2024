from collections import defaultdict

input = open("inputs/day08.txt").read().split("\n")
antennas = defaultdict(list)
for y, line in enumerate(input):
    for x, c in enumerate(line):
        if c != ".":
            antennas[c].append((y, x))

def inbounds(y, x):
    return 0 <= y < len(input) and 0 <= x < len(input[0])

def add_inbounds(s, val):
    if inbounds(*val):
        s.add(val)

antinodes = set()
antinodes2 = set()
for antenna, coords in antennas.items():
    for i, (ay, ax) in enumerate(coords):
        for (by, bx) in coords[i+1:]:
            dy, dx = ay - by, ax - bx
            add_inbounds(antinodes, (ay + dy, ax + dx))
            add_inbounds(antinodes, (by - dy, bx - dx))
            y, x = ay, ax
            while inbounds(y, x):
                antinodes2.add((y, x))
                y, x = y + dy, x + dx
            y, x = ay, ax
            while  inbounds(y, x):
                antinodes2.add((y, x))
                y, x = y - dy, x - dx

print(f"part 1 = {len(antinodes)}")
print(f"part 2 = {len(antinodes2)}")
