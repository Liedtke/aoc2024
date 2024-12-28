from collections import deque
max_corruptions = 1024
input = [tuple(map(int, line.split(","))) for line in open("inputs/day18.txt").read().split("\n")]
max_x, max_y = (max(n for n in dim) for dim in zip(*input))

grid = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]

for x, y in input[:max_corruptions]:
    grid[y][x] = True

visited = set()
queue = deque(((0, 0, 0),))
while queue:
    y, x, count = queue.popleft()
    if y == max_y and x == max_x:
        print(f"part 1 = {count}")
        break
    if (y, x) not in visited:
        visited.add((y, x))
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny <= max_y and 0 <= nx <= max_x and not grid[ny][nx]:
                queue.append((ny, nx, count+1))
