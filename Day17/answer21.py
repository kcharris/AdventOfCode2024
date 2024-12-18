f = open("Day17\data.txt")
# f = open("Day17\data2.txt")

reg = {"A":0, "B":0, "C":0}
program = None
ins_ptr = [0]
output = []
for line in f.readlines():
    line = line.rstrip()
    if line == "":
        continue
    if line[0] == "R":
        _, r, snum = line.split()
        reg[r[0]] = int(snum)
    if line[0] == "P":
        _, p = line.split()
        program = list(map(int, p.split(",")))

def dataCycle(a):
    b = a % 8
    b ^= 3
    c = a // (2**b)
    b ^= c
    b ^= 5
    return b % 8

def data2Cycle(a):
    return a % 8

M = 10**20
output = [-1 for _ in range(len(program))]
def helper(a, r):
    print(a, r, output, program)
    if r == -1:
        if output == program:
            return a
    res = M
    prev_r = output[r]
    for i in range(8):
        next_a = (a<<3) + i
        output[r] = dataCycle(next_a)
        if output[r] == program[r]:
            res = min(res, helper(next_a, r-1))
    output[r] = prev_r
    return res

res = helper(0, len(output)-1)
print(res)

    
    