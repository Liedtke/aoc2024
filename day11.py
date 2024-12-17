
input = list(map(int, open("inputs/day11.txt").read().split(" ")))
for gen in range(25):
    next = []
    for stone in input:
        if stone == 0:
            next.append(1)
            continue
        as_string = str(stone)
        if len(as_string) % 2 == 0:
            split = len(as_string) // 2
            next.append(int(as_string[:split]))
            next.append(int(as_string[split:]))
        else:
            next.append(stone * 2024)
    input = next
    print(f"gen {gen}: {len(input)}")
