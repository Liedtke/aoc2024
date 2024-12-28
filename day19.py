towels, patterns = open("inputs/day19.txt").read().split("\n\n")
towels, patterns = set(towels.split(", ")), patterns.split("\n")
res = 0
max_towel_len = max(map(len, towels))
for pattern in patterns:
    tried = set()
    print(pattern)
    starts = [0]
    while starts:
        s = starts.pop()
        tried.add(s)
        if s == len(pattern):
            res += 1
            break
        for i in range(1, min(len(pattern) - s, max_towel_len) + 1):
            if pattern[s:s+i] in towels and s+i not in tried:
                starts.append(s+i)
print(f"part 1 = {res}")
