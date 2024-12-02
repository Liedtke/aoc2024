lists = [tuple(map(int, line.split("   "))) for line in open("inputs/day01.txt").read().split("\n")]
lists = [sorted(li) for li in zip(*lists)]
print(f"part 1 = {sum(abs(x - y) for x, y in zip(*lists))}")
print(f"part 2 = {sum(sum(1 for x in lists[1] if x == value) * value for value in lists[0])}")
