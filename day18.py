from collections import deque
max_corruptions = 1024
input = [tuple(map(int, line.split(","))) for line in open("inputs/day18.txt").read().split("\n")]
max_x, max_y = (max(n for n in dim) for dim in zip(*input))

def create_grid(count):
    grid = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]
    for x, y in input[:count]:
        grid[y][x] = True
    return grid

def find_path(grid):
    visited = set()
    queue = deque(((0, 0, 0),))
    while queue:
        y, x, count = queue.popleft()
        if y == max_y and x == max_x:
            return count
        if (y, x) not in visited:
            visited.add((y, x))
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny <= max_y and 0 <= nx <= max_x and not grid[ny][nx]:
                    queue.append((ny, nx, count+1))
    return None

print(f"part 1 = {find_path(create_grid(max_corruptions))}")
lower, upper = (0, len(input))
while lower != upper:
    pivot = lower + (upper - lower) // 2
    res = find_path(create_grid(pivot))
    if res is None:
        upper = pivot
    else:
        lower = pivot + 1
print(f"part 2 = {','.join(map(str, input[lower-1]))}")
