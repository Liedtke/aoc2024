import operator

def rec(operands, ops, expected, idx, value):
    if value > expected:
        return False
    if idx == len(operands):
        return value == expected
    return any(rec(operands, ops, expected, idx+1, op(value, operands[idx])) for op in ops)

input = (line.split(": ") for line in open("inputs/day07.txt").read().split("\n"))
input = [(int(lhs), tuple(map(int, rhs.split(" ")))) for lhs, rhs in input]
results = [0, 0]
concat = lambda a, b: int(str(a) + str(b))
for i, operators in enumerate(((operator.add, operator.mul), (operator.add, operator.mul, concat))):
    for expected, operands in input:
        if rec(operands, operators, expected, 1, operands[0]):
            results[i] += expected

print(f"part 1 = {results[0]}")
print(f"part 2 = {results[1]}")
