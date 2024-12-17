from collections import deque
input = [[int(n) for n in line] for line in open("inputs/day10.txt").read().split("\n")]

def evaluate(y, x, is_part2):
    counts = [[0 for _ in line] for line in input]
    counts[y][x] = 1
    pushed = set([(y, x)])
    queue = deque([(y, x)])
    result = 0
    while queue:
        y, x = queue.popleft()
        val = input[y][x]
        if val == 9:
            result += counts[y][x] if is_part2 else 1
        for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(input) and 0 <= nx < len(input[ny]) and input[ny][nx] == val + 1:
                counts[ny][nx] += counts[y][x]
                if (ny, nx) not in pushed:
                    pushed.add((ny, nx))
                    queue.append((ny, nx))
    return result

print(f"part 1 = {sum(sum(evaluate(y, x, False) for x, val in enumerate(line) if val == 0) for y, line in enumerate(input))}")
print(f"part 2 = {sum(sum(evaluate(y, x, True) for x, val in enumerate(line) if val == 0) for y, line in enumerate(input))}")
