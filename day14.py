import functools, operator, re
regex = re.compile(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
input = [[int(x) for x in m] for m in regex.findall(open("inputs/day14.txt").read())]
dim_x, dim_y = [max(x) + 1 for x in tuple(zip(*input))[0:2]]
positions = [((sx + dx * 100) % dim_x, (sy + dy * 100) % dim_y) for sx, sy, dx, dy in input]
quadrants = [int(x > dim_x // 2) + int(y > dim_y // 2) * 2 for x, y in positions
             if x != dim_x // 2 and y != dim_y // 2]
counts = [0] * 4
for q in quadrants:
    counts[q] += 1
print(f"part 1 = {functools.reduce(operator.mul, counts, 1)}")
