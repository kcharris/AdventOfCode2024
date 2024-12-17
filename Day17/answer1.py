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
    res = -1
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
    elif ins == 6:
        reg["B"] = reg["A"] // 2**getOperand(op)
    elif ins == 7:
        reg["C"] = reg["A"] // 2**getOperand(op)

while ins_ptr[0] < len(program)-1:
    ins = program[ins_ptr[0]]
    op = program[ins_ptr[0]+1]
    doInstruction(ins, op)
    ins_ptr[0] += 2

print(",".join(list(map(str, output))))