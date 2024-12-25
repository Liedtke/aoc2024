reg, program = open("inputs/day17.txt").read().split("\n\n")
regs = [int(r[12:]) for r in reg.split("\n")]
program = [int(n) for n in program[9:].split(",")]
pc = 0
output = []

def combo(op):
    return regs[op - 4] if 4 <= op <= 6 else op

def adv(a):
    regs[0] = regs[0] >> combo(a)
def bxl(a):
    regs[1] ^= a
def bst(a):
    regs[1] = combo(a) & 7
def jnz(a):
    if regs[0] != 0:
        global pc
        pc = a - 2
def bxc(_):
    regs[1] ^= regs[2]
def out(a):
    output.append(combo(a) & 7)
def bdv(a):
    regs[1] = regs[0] >> combo(a)
def cdv(a):
    regs[2] = regs[0] >> combo(a)

ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
def run():
    global pc
    try:
        while True:
            op = program[pc+1]
            ops[program[pc]](op)
            pc += 2
    except IndexError:
        return output

run()
print(f"part 1 = {','.join(map(str, output))}")


def try_it(val, num_matched):
    global pc
    global output
    pc = 0
    regs[0] = val
    output = []
    run()
    if len(output) <= num_matched:
        return -1
    for i, v in enumerate(reversed(output)):
        if v != program[-i-1]:
            return -1
    return len(output)

def part2(expected, inputs, num_matched):
    if num_matched == len(expected):
        return inputs
    bits = 3 # This could also be increased iteratively from 0.
    res = []
    new_num_matched = 0
    for input in inputs:
        input = input << bits
        for i in range(1 << bits):
            val = input + i
            matched = try_it(val, num_matched)
            if matched > num_matched:
                new_num_matched = matched
                res.append(val)
    return part2(expected, res, new_num_matched)

print(f"part 2 = {min(part2(program, [0], 0))}")
