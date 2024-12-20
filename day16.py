import heapq, math
dirs = [
    ( 0,  1), #E
    ( 1,  0), #S
    ( 0, -1), #W
    (-1,  0), #N
]
maze = open("inputs/day16.txt").readlines()
y, x = (len(maze) - 2, 1)
assert maze[y][x] == "S"
heap = [(0, (y, x), 0)]
min_scores = [[math.inf for _ in line] for line in maze]
while maze[y][x] != "E":
    (score, (y, x), direction) = heapq.heappop(heap)
    ny, nx = y + dirs[direction][0], x + dirs[direction][1]
    field = maze[ny][nx]
    if (field == "." or field == "E") and score+1 < min_scores[ny][nx]:
        min_scores[ny][nx] = score+1
        heapq.heappush(heap, (score+1, (ny, nx), direction))
    for next_dir in ((direction-1) % 4, (direction+1) % 4):
        ny, nx = y + dirs[next_dir][0], x + dirs[next_dir][1]
        field = maze[ny][nx]
        if (field == "." or field == "E") and score+1001 < min_scores[ny][nx]:
            heapq.heappush(heap, (score + 1001, (ny, nx), next_dir))
print(f"part 1 = {score}")
