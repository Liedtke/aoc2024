import functools, operator, re
regex = re.compile(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
input_data = [[int(x) for x in m] for m in regex.findall(open("inputs/day14.txt").read())]
dim_x, dim_y = [max(x) + 1 for x in tuple(zip(*input_data))[0:2]]
positions = [((sx + dx * 100) % dim_x, (sy + dy * 100) % dim_y) for sx, sy, dx, dy in input_data]
quadrants = [int(x > dim_x // 2) + int(y > dim_y // 2) * 2 for x, y in positions
             if x != dim_x // 2 and y != dim_y // 2]
counts = [0] * 4
for q in quadrants:
    counts[q] += 1
print(f"part 1 = {functools.reduce(operator.mul, counts, 1)}")

def part2():
    for i in range(10_000):
        robot_pos = [((sx + dx * i) % dim_x, (sy + dy * i) % dim_y) for sx, sy, dx, dy in input_data]
        robot_map = [[0] * dim_x for _ in range(dim_y)]
        for x, y in robot_pos:
            robot_map[y][x] += 1
        # Search for a vertical line.
        for y in range(0, dim_y - 7, 7):
            for x, c in enumerate(robot_map[y]):
                if c > 0 and robot_map[y+1][x] == c and robot_map[y+2][x] == c \
                         and robot_map[y+3][x] == c and robot_map[y+4][x] == c \
                         and robot_map[y+5][x] == c and robot_map[y+6][x] == c:
                    # print(f"=== After {i} seconds ===")
                    # print("\n".join("".join(map(str, line)) for line in robot_map))
                    return i

print(f"part 2 = {part2()}")
