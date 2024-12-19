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

warehouse, movements = open("inputs/day15.txt").read().split("\n\n")
warehouse, movements = [list(line) for line in warehouse.split("\n")], movements.replace("\n", "")
ry, rx = next((y, line.index("@")) for y, line in enumerate(warehouse) if "@" in line)
warehouse[ry][rx]= "." # For simplicity, remove robot from the map.
part1(warehouse[:], movements, ry, rx)
