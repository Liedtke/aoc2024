reg, program = open("inputs/day17b.txt").read().split("\n\n")
regs = [int(r[12:]) for r in reg.split("\n")]
program = [int(n) for n in program[9:].split(",")]
pc = 0
output = []

def combo(op):
    return regs[op - 4] if 4 <= op <= 6 else op

def adv(a):
    regs[0] = regs[0] // (2 ** combo(a))
def bxl(a):
    regs[1] = regs[1] ^ a
def bst(a):
    regs[1] = combo(a) % 8
def jnz(a):
    if regs[0] != 0:
        global pc
        pc = a - 2
def bxc(_):
    regs[1] = regs[1] ^ regs[2]
def out(a):
    output.append(combo(a) % 8)
def bdv(a):
    regs[1] = regs[0] // (2 ** combo(a))
def cdv(a):
    regs[2] = regs[0] // (2 ** combo(a))

ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
try:
    while True:
        op = program[pc+1]
        ops[program[pc]](op)
        pc += 2
except IndexError:
    print(",".join(map(str, output)))
