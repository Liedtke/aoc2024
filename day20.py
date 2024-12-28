grid = open("inputs/day20.txt").read().split("\n")
start = next(((y, line.index("S")) for y, line in enumerate(grid) if "S" in line))
grid = [[c for c in line] for line in grid]
path = [start]
y, x = start
grid[y][x] = 1
finished = False
while not finished:
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny, nx = y + dy, x + dx
        finished = grid[ny][nx] == "E"
        if grid[ny][nx] == "." or finished:
            path.append((ny, nx))
            grid[ny][nx] = len(path)
            y, x = ny, nx
            break

limit = 100
cheats = 0
for y, x in path:
    for dy, dx in ((2, 0), (0, 2), (-2, 0), (0, -2)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and isinstance(grid[ny][nx], int) \
            and grid[ny][nx] >= grid[y][x] + limit + 2:
            cheats += 1
print(f"part 1 = {cheats}")

cheats2 = 0
length = 20
for y, x in path:
    for dy in range(-length, length+1):
        ny = y + dy
        if 0 <= ny < len(grid):
            for dx in range(-(length-abs(dy)), length-abs(dy)+1):
                nx = x + dx
                if 0 <= nx < len(grid[ny]) and isinstance(grid[ny][nx], int) \
                    and grid[ny][nx] >= grid[y][x] + limit + abs(dy) + abs(dx):
                        cheats2 += 1
print(f"part 2 = {cheats2}")
