from collections import defaultdict

input = {stone: 1 for stone in map(int, open("inputs/day11.txt").read().split(" "))}
for gen in range(75):
    next = defaultdict(int)
    for stone, count in input.items():
        if stone == 0:
            next[1] += count
            continue
        as_string = str(stone)
        if len(as_string) % 2 == 0:
            split = len(as_string) // 2
            next[int(as_string[:split])] += count
            next[int(as_string[split:])] += count
        else:
            next[stone * 2024] += count
    input = next
    if gen == 24 or gen == 74:
        print(f"part {1 if gen == 24 else 2} = {sum(n for n in input.values())}")
