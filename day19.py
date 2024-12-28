import heapq
from collections import defaultdict
towels, patterns = open("inputs/day19.txt").read().split("\n\n")
towels, patterns = set(towels.split(", ")), patterns.split("\n")
patterns_1 = set()
part_2 = 0
pattern_counts = {towel: 1 for towel in towels}

for pattern in patterns:
    counts = defaultdict(int)
    counts[0] = 1
    starts = [0]
    while starts:
        s = heapq.heappop(starts)
        if s == len(pattern):
            patterns_1.add(pattern)
        for i in range(1, len(pattern) - s + 1):
            if pattern[s:s+i] in towels:
                if s+i not in counts:
                    heapq.heappush(starts, s+i)
                counts[s+i] += counts[s]
    part_2 += counts[len(pattern)]
print(f"part 1 = {len(patterns_1)}")
print(f"part 2 = {part_2}")
