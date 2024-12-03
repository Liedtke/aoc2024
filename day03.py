import re
regex_mul = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
input = open("inputs/day03.txt").read()
print(f"part 1 = {sum(int(match[0]) * int(match[1]) for match in regex_mul.findall(input))}")

regex_op = re.compile(r"(mul|do|don't)\((([0-9]+),([0-9]+))?\)")
enabled = True
result = 0
for op, _, a, b in regex_op.findall(input):
    if op == "do":
        enabled = True
    elif op == "don't":
        enabled = False
    else:
        assert op == "mul"
        if enabled:
            result += int(a) * int(b)
print(f"part 2 = {result}")
