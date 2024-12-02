def is_valid(values):
    prev = values[0]
    asc = values[1] > values[0]
    for v in values[1:]:
        if asc != (v > prev) or not (1 <= abs(v - prev) <= 3):
            return False
        prev = v
    return True

reports = [[int(n) for n in line.split(" ")] for line in open("inputs/day02.txt").read().split("\n")]
print(f"part 1 = {sum(is_valid(r) for r in reports)}")
# Brute force: Just try out removing each element until we find a valid combination.
print(f"part 2 = {sum(any(is_valid(r[:i] + r[i+1:]) for i in range(len(r))) for r in reports)}")
