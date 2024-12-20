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
min_scores = [[[[math.inf, None, y, x] for x, _ in enumerate(line)] for y, line in enumerate(maze)] for _ in dirs]
min_scores[0][y][x][0] = 0
heap = [(0, (y, x), 0)]
best = (math.inf, None)
ey, ex = None, None

def update_and_queue(ny, nx, n_dir, score, predecessors):
    if score < min_scores[n_dir][ny][nx][0]:
        min_scores[n_dir][ny][nx][0] = score
        min_scores[n_dir][ny][nx][1] = [predecessors]
        heapq.heappush(heap, (score, (ny, nx), n_dir))
    else:
        min_scores[n_dir][ny][nx][1].append(predecessors)

while heap:
    (score, (y, x), direction) = heapq.heappop(heap)
    if score > best[0]:
        continue
    if maze[y][x] == "E":
        if score < best[0]:
            best = (score, direction)
        assert score > best[0] or direction == best[1], "Other cases unimplemented"
        ey, ex = (y, x)
        continue
    ny, nx = y + dirs[direction][0], x + dirs[direction][1]
    field = maze[ny][nx]
    score_n = score + 1
    if (field == "." or field == "E") and score_n <= min_scores[direction][ny][nx][0]:
        update_and_queue(ny, nx, direction, score+1, min_scores[direction][y][x])
    for next_dir in ((direction-1) % 4, (direction+1) % 4):
        ny, nx = y + dirs[next_dir][0], x + dirs[next_dir][1]
        field = maze[ny][nx]
        if (field == "." or field == "E") and score+1001 <= min_scores[next_dir][ny][nx][0]:
            update_and_queue(ny, nx, next_dir, score+1001, min_scores[direction][y][x])

print(f"part 1 = {best[0]}")
visited = set()
to_visit = [min_scores[best[1]][ey][ex]]
while to_visit:
    score, predecessors, y, x = to_visit.pop()
    visited.add((y, x))
    if predecessors is not None:
        for p in predecessors:
            to_visit.append(p)

print(f"part 2 = {len(visited)}")
