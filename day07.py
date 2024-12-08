import operator
import itertools

input = (line.split(": ") for line in open("inputs/day07.txt").read().split("\n"))
input = [(int(lhs), tuple(map(int, rhs.split(" ")))) for lhs, rhs in input]
part_1 = 0
for expected, operands in input:
    for operators in itertools.product(*([(operator.add, operator.mul)] * (len(operands)-1))):
        result = operands[0]
        for operand, op in zip(operands[1:], operators):
            result = op(result, operand)
        if result == expected:
            part_1 += expected
            break

print(f"part 1 = {part_1}")
