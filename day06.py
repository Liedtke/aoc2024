input = open("inputs/day06.txt").read().split("\n")
# Possible directions array.
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 0
dy, dx = dirs[i]
# Get start position.
for y, line in enumerate(input):
    if "^" in line:
        x = line.index("^")
        break
start = y, x

visited = [[False for _ in line] for line in input]
try:
    while True:
        visited[y][x] = True
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0:
            raise IndexError
        if input[ny][nx] == "#":
            i = (i + 1) % len(dirs)
            dy, dx = dirs[i]
            continue
        y, x = ny, nx
except IndexError:
    print(f"part 1 = {sum(sum(v for v in line) for line in visited)}")
