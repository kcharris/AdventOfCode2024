f = open("Day17\data.txt")
# f = open("Day17\data1.txt")

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
    
def getOperand(num):
    if num >= 0 and num <= 3:
        return num
    if num == 4:
        return reg["A"]
    if num == 5:
        return reg["B"]
    else:
        return reg["C"]

def doInstruction(ins, op):
    if ins == 0:
        reg["A"] = reg["A"] // 2**getOperand(op)
    elif ins == 1:
        reg["B"] ^= op
    elif ins == 2:
        reg["B"] = getOperand(op) % 8
    elif ins == 3:
        if reg["A"] != 0:
            # sub by 2 to get ins_ptr = op after running
            ins_ptr[0] = op - 2
    elif ins == 4:
        reg["B"] = reg["B"] ^ reg["C"]
    elif ins == 5:
        output.append(getOperand(op) % 8)
        x = len(output) -1
        if output[x] != program[x]:
            return 0
    elif ins == 6:
        reg["B"] = reg["A"] // 2**getOperand(op)
    elif ins == 7:
        reg["C"] = reg["A"] // 2**getOperand(op)
    
    return 1

# can this be reverse engineered?
def revInstruction(ins, op):
    # rev
    if ins == 0:
        reg["A"] = reg["A"] * 2**getOperand(op)
    # already rev
    elif ins == 1:
        reg["B"] ^= op
    # ???
    elif ins == 2:
        reg["B"] = 0 # getOperand(op) % 8
    # will need reverse look ahead of 2 on each ins call. Might need to move to top
    elif ins == 3:
        if reg["A"] != 0:
            # sub by 2 to get ins_ptr = op after running
            ins_ptr[0] = op - 2
    # already rev
    elif ins == 4:
        reg["B"] ^= reg["C"]
    # rev output by appending to front
    elif ins == 5:
        output.insert(0, getOperand(op) % 8)
        x = len(output)
        if output[0] != program[len(program) - x]:
            return 0
    # rev
    elif ins == 6:
        reg["B"] = reg["A"] * 2**getOperand(op)
    # rev
    elif ins == 7:
        reg["C"] = reg["A"] * 2**getOperand(op)
    
    return 1

def doProgram(program):
    while ins_ptr[0] < len(program)-1:
        ins = program[ins_ptr[0]]
        op = program[ins_ptr[0]+1]
        res = doInstruction(ins, op)
        if res == 0:
            return 0
        ins_ptr[0] += 2

    return ",".join(list(map(str, output)))

for i in range(10**8):
    ins_ptr = [0]
    output = []
    reg["A"] = i
    reg["B"] = 0
    reg["C"] = 0

    out_str = doProgram(program)
    if out_str != 0:
        print(i, out_str)
    if out_str == 0:
        continue
    p_str = ",".join(list(map(str, program)))
    if out_str == p_str:
        print(i)
        break

