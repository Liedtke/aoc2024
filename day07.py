import operator

def rec(operands, ops):
    if len(operands) == 1:
        return operands
    inner_values = rec(operands[:-1], ops)
    res = set()
    for inner in inner_values:
        for inner_res in (op(inner, operands[-1]) for op in ops):
            res.add(inner_res)
    return res

input = (line.split(": ") for line in open("inputs/day07.txt").read().split("\n"))
input = [(int(lhs), tuple(map(int, rhs.split(" ")))) for lhs, rhs in input]
results = [0, 0]
concat = lambda a, b: int(str(a) + str(b))
for i, operators in enumerate(((operator.add, operator.mul), (operator.add, operator.mul, concat))):
    for expected, operands in input:
        res = rec(operands, operators)
        if expected in res:
            results[i] += expected


print(f"part 1 = {results[0]}")
print(f"part 2 = {results[1]}")
