input = open("inputs/day12.txt").read().split("\n")
marked = [[False for _ in line] for line in input]
#              up       right    down    left
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def in_bounds(y, x):
    return 0 <= y < len(input) and 0 <= x < len(input[y])

def explore_region(y, x):
    val = input[y][x]
    perimeter1, perimeter2, area = 0, 0, 0
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        assert input[y][x] == val
        if marked[y][x]:
            continue
        marked[y][x] = True
        area += 1

        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx
            if in_bounds(ny, nx) and input[ny][nx] == val:
                stack.append((ny, nx))
            else: # Not the same region, needs fence.
                perimeter1 += 1
                # For part 2 check the adjacent values as well. (Check if this fence is a continuation of an existing fence.)
                dy, dx = directions[i - 1]
                py, px = y + dy, x + dx
                npy, npx = ny + dy, nx + dx
                if not in_bounds(py, px) or input[py][px] != val or (in_bounds(npy, npx) and input[npy][npx] == val):
                    perimeter2 += 1

    # print(f"region {val}: area={area} perimeter1={perimeter1} price1={area*perimeter1} perimeter2={perimeter2} price2={area*perimeter2}")
    return area * perimeter1, area * perimeter2

results = [0, 0]
for y, line in enumerate(input):
    for x, _ in enumerate(line):
        if not marked[y][x]:
            results = [a + b for a, b in zip(results, explore_region(y, x))]

print(f"part 1 = {results[0]}")
print(f"part 2 = {results[1]}")
