import itertools

input = [line for line in open("inputs/day04.txt").read().split("\n")]

def test1(x, y, dx, dy):
    expected = "MAS"
    try:
        for e in expected:
            x += dx
            y += dy
            if x < 0 or y < 0 or input[y][x] != e:
                return 0
        return 1
    except:
        return 0

result1 = 0
result2 = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "X":
            result1 += sum(test1(x, y, dx, dy) for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1)))
        elif char == "A" and 0 < x < len(line)-1 and 0 < y < len(input)-1:
            count_mas = sum(input[y + dy][x + dx] == "M" and input[y - dy][x - dx] == "S"
                            for dx, dy in itertools.product((-1, 1), (-1, 1)))
            result2 += count_mas == 2

print(f"part 1 = {result1}")
print(f"part 2 = {result2}")
