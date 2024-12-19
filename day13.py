import re
regex = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)\nButton B: X\+([0-9]+), Y\+([0-9]+)\nPrize: X=([0-9]+), Y=([0-9]+)")

def solve(offset):
    result = 0
    for input in open("inputs/day13.txt").read().split("\n\n"):
        x1, y1, x2, y2, tx, ty = [int(x) for x in regex.match(input).groups()]
        tx, ty = tx + offset, ty + offset
        # linear equations:
        #   x1 * a + x2 * b = tx    (1)
        #   y1 * a + y2 * b = ty    (2)
        # - transform (2):
        #   b = (ty - y1 * a) / y2  (3)
        # - insert (3) in (1):
        #   x1 * a + x2 * (ty - y1 * a) / y2 = tx
        #   x1 * a + x2 * ty / y2 - x2 * y1 / y2 * a = tx
        #   x1 * a - x2 * y1 / y2 * a = tx - x2 * ty / y2
        #   (x1 - x2 * y1 / y2) * a = tx - x2 * ty / y2
        #   a = (tx - x2 * ty / y2) / (x1 - x2 * y1 / y2)
        #   a = (tx * y2 - x2 * ty) / (x1 * y2 - x2 * y1)
        a = (tx * y2 - x2 * ty) / (x1 * y2 - x2 * y1)
        b = (ty - y1 * a) / y2
        if a.is_integer() and b.is_integer():
            result += int(a * 3 + b)
    return result

print(f"part 1 = {solve(0)}")
print(f"part 2 = {solve(10000000000000)}")
