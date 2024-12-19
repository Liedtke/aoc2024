import math, re
regex = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)\nButton B: X\+([0-9]+), Y\+([0-9]+)\nPrize: X=([0-9]+), Y=([0-9]+)")

def solve(offset):
    result = 0
    for input in open("inputs/day13e.txt").read().split("\n\n"):
        x1, y1, x2, y2, tx, ty = [int(x) for x in regex.match(input).groups()]
        tx, ty = tx + offset, ty + offset
        min_tokens = math.inf
        for i in range(101):
            x, y = x1 * i, y1 * i
            dx, dy = tx - x, ty - y
            steps_x, steps_y = dx / x2, dy / y2
            if steps_x == steps_y == math.floor(steps_x):
                print(f"possible combination: {i}, {steps_x}")
                min_tokens = int(min(min_tokens, i * 3 + steps_x))
        print(min_tokens)
        result += min_tokens if min_tokens != math.inf else 0
    return result

print(f"part 1 = {solve(0)}")
