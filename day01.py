lists = [tuple(map(int, line.split("   "))) for line in open("inputs/day01.txt").read().split("\n")]
lists = [sorted(pair[i] for pair in lists) for i in range(2)]
print(f"part 1 = {sum(abs(x - y) for x, y in zip(lists[0], lists[1]))}")
print(f"part 2 = {sum(sum(1 for x in lists[1] if x == value) * value for value in lists[0])}")
