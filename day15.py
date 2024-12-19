dirs = {
    "<": ( 0, -1),
    ">": ( 0,  1),
    "^": (-1,  0),
    "v": ( 1,  0),
}

def part1(warehouse, movements, ry, rx):
    for move in movements:
        dy, dx = dirs[move]
        ny, nx = ry + dy, rx + dx
        field = warehouse[ny][nx]
        if field == ".":
            ry, rx = ny, nx # Move robot.
        else:
            cy, cx = ny, nx
            while field == "O":
                cy, cx = cy + dy, cx + dx
                field = warehouse[cy][cx]
            if field == ".":  # Move robot and crates.
                ry, rx = ny, nx
                warehouse[ny][nx] = "."
                warehouse[cy][cx] = "O"
    print(f"part 1 = {sum(sum(100 * y + x for x, c in enumerate(line) if c == 'O') for y, line in enumerate(warehouse))}")

def part2(warehouse, movements, ry, rx):
    for move in movements:
        dy, dx = dirs[move]
        ny, nx = ry + dy, rx + dx
        field = warehouse[ny][nx]
        if field == ".":
            ry, rx = ny, nx # Move robot.
        else:
            cy, cx = ny, nx
            if move in "<>":
                while field in "[]":
                    cx = cx + dx * 2
                    field = warehouse[cy][cx]
                    if field == ".":
                        rx = nx # Move robot.
                        warehouse[ry][rx] = "."
                        for x in range(rx+1, cx+1, 2) if move == ">" else range(cx, rx, 2):
                            warehouse[ry][x] = "["
                            warehouse[ry][x+1] = "]"
            else:
                pos_to_check = [(cy, cx)]
                crates_to_move = []
                while pos_to_check:
                    cy, cx = pos_to_check.pop()
                    field = warehouse[cy][cx]
                    if field in "[]":
                        cx -= field == "]"
                        crates_to_move.append((cy, cx))
                        pos_to_check.append((cy + dy, cx))
                        pos_to_check.append((cy + dy, cx + 1))
                    elif field == "#":
                        pos_to_check.append(None) # dummy entry
                        break
                if not pos_to_check:
                    ry = ny # Move robot.
                    for y, x in crates_to_move:
                        warehouse[y][x] = "."
                        warehouse[y][x+1] = "."
                    for y, x in crates_to_move:
                        warehouse[y+dy][x] = "["
                        warehouse[y+dy][x+1] = "]"
    print(f"part 2 = {sum(sum(100 * y + x for x, c in enumerate(line) if c == '[') for y, line in enumerate(warehouse))}")

warehouse, movements = open("inputs/day15.txt").read().split("\n\n")
warehouse, movements = [list(line) for line in warehouse.split("\n")], movements.replace("\n", "")
ry, rx = next((y, line.index("@")) for y, line in enumerate(warehouse) if "@" in line)
warehouse[ry][rx]= "." # For simplicity, remove robot from the map.
warehouse2 = [list("".join(line).replace(".", "..").replace("#", "##").replace("O", "[]")) for line in warehouse]
part1(warehouse, movements, ry, rx)
part2(warehouse2, movements, ry, rx * 2)
