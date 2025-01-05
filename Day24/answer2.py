import re
import matplotlib.pyplot as plt
from random import randint

def getAndParseInput():
    f = open("Day24\data.txt")
    arr = f.readlines()
    initial = []
    gates = []
    i = 0
    while arr[i] != "\n":
        initial.append(arr[i].rstrip())
        i+=1
    i += 1
    while i < len(arr):
        gates.append(arr[i].rstrip())
        i+=1

    initial_wires = {}
    for s in initial:
        m = re.findall(r"([\d\w]{3}): (\d)", s)
        a, b = m[0]
        initial_wires[a] = int(b)

    gate_arr = []
    for s in gates:
        m = re.findall(r"([\d\w]{3}) (\w+) ([\d\w]{3}) -> ([\d\w]{3})", s)
        gate_arr.append(list(m[0]))
    return gate_arr, initial_wires
gate_arr, initial_wires = getAndParseInput()

def setRandInitialWires(d):
    def setLetter(l, d):
        x = randint(10**14, 10**15)
        i = 0
        while x > 0:
            key = "{}{:02d}".format(l, i)
            if key not in d:
                break
            else:
                curr_bit = x % 2
                x //= 2
                d[key] = curr_bit
            i += 1
    setLetter("x", d)
    setLetter('y', d)

# Attempt to deduce and the unknown wire values based on boolean logic
# Allows the option to set initial x and y values to random numbers
def getWires(initial_wires, gate_arr, random_xy=False):
    d = initial_wires.copy()
    if random_xy == True:
        setRandInitialWires(d)
    for m in gate_arr:
        for a in m:
            if a not in d:
                d[a] = None
    if "OR" in d: del d["OR"]
    if "AND" in d: del d["AND"]
    if "XOR" in d: del d["XOR"]

    found = set()
    for k in d:
        if d[k] != None:
            found.add(k)
    prev = 0
    count = -1
    while len(d.keys()) > len(found) and prev != count:
        prev = count
        count = 0
        for a, op, b, c in gate_arr:
            if d[a] == None or d[b] == None or d[c] == None:
                if op == "OR":
                    if d[a] != None and d[b] != None:
                        d[c] = d[a] | d[b]
                        found.add(c)
                    if d[a] == 1:
                        d[c] = 1
                        found.add(a)
                    if d[b] == 1:
                        d[c] = 1
                        found.add(b)
                    if d[c] == 0:
                        d[a] = 0
                        d[b] = 0
                        found.add(a)
                        found.add(b)
                elif op == "AND":
                    if d[a] != None and d[b] != None:
                        d[c] = d[a] & d[b]
                        found.add(c)
                    if d[c] != None:
                        if d[c] == 1:
                            d[a] = 1
                            d[b] = 1
                            found.add(a)
                            found.add(b)
                        # c == 0
                        elif d[a] == 1:
                            d[b] = 0
                            found.add(b)
                        elif d[b] == 1:
                            d[a] = 0
                            found.add(a)
                    elif d[a] == 0:
                        d[c] = 0
                        found.add(c)
                    elif d[b] == 0:
                        d[c] = 0
                        found.add(c)
                elif op == "XOR":
                    if d[a] != None and d[b] != None:
                        d[c] = d[a] ^ d[b]
                        found.add(c)
                    if d[b] != None and d[c] != None:
                        d[a] = d[b] ^ d[c]
                        found.add(a)
                    if d[a] != None and d[c] != None:
                        d[b] = d[a] ^ d[c]
                        found.add(b)
            else:
                count += 1
    return d

def wireNumAndMSB(d, l):
    bit_arr = []
    for i in range(99, -1,-1):
        key = "{}{:02d}".format(l, i)
        if key in d:
            bit_arr.append(d[key])
    return int("".join(map(str, bit_arr)),2), len(bit_arr)

def isValidXYZ(d):
    for k in d:
        if d[k] == None:
            return False
    x, x_msb = wireNumAndMSB(d, "x")
    y, y_msb = wireNumAndMSB(d, "y")
    z, z_msb = wireNumAndMSB(d, "z")
    if (x + y) % 2**(z_msb) == z:
        return True
    return False

# Uses properties of ALU's full adder required output gates to get easy to find bad wires.
def getBadIdxs():
    start_wires = ["y", "x"]
    bad_idxs = []
    for i in range(len(gate_arr)):
        a, b, c, d = gate_arr[i]
        if (
            d[0] == "z" and b != "XOR" # and
            # a[0] in start_wires and c[0] in start_wires
            ):
            bad_idxs.append(i)
        if (
            a[0] not in start_wires and
            c[0] not in start_wires and
            b == "XOR" and 
            d[0] != "z"
            ):
            bad_idxs.append(i)
    return bad_idxs

def isValidGateArr(gate_arr, times=5):
    for _ in range(times):
        updated_d = getWires(initial_wires, gate_arr, random_xy=True)
        if isValidXYZ(updated_d) == False:
            return False
    return True

def findWrongBits(x, y, z):
    count = 0
    wrong_bits = []
    wire_sum = x + y
    while z > 0:
        if z % 2 != wire_sum % 2:
            wrong_bits.append(count)
        z //= 2
        wire_sum //= 2
        count += 1
    return wrong_bits[::-1]

bad_idxs = getBadIdxs()
print("Bad z's: ", "".join(sorted([str((gate_arr[i][3], i)) for i in bad_idxs])))
nonz = list(map(lambda i: (gate_arr[i][3], i), filter(lambda i: gate_arr[i][3][0] != "z", bad_idxs)))
hasz = list(map(lambda i: (gate_arr[i][3], i), filter(lambda i: gate_arr[i][3][0] == "z", bad_idxs)))
hasz.remove(("z45", 52))

def dfs(visited):
    if len(visited) == 6:
        for i in range(len(gate_arr)):
            if i not in visited:
                visited.add(i)
                for j in range(len(gate_arr)):
                    if j not in visited:
                        visited.add(j)
                        gate_arr[i][3], gate_arr[j][3] = gate_arr[j][3], gate_arr[i][3]
                        flag = True
                        if isValidGateArr(gate_arr, times=20):
                            print([(gate_arr[k][3], k) for k in visited])
                            print(",".join(sorted(map(lambda a: gate_arr[a][3], visited))))
                        visited.remove(j)
                        gate_arr[i][3], gate_arr[j][3] = gate_arr[j][3], gate_arr[i][3]
                visited.remove(i)
        return 0
    res = None
    for k1, i in nonz:
        if i not in visited:
            visited.add(i)
            for k2, j in hasz:
                if j not in visited:
                    visited.add(j)
                    gate_arr[i][3], gate_arr[j][3] = gate_arr[j][3], gate_arr[i][3]
                    curr = dfs(visited)
                    if curr != None:
                        res = curr
                    gate_arr[i][3], gate_arr[j][3] = gate_arr[j][3], gate_arr[i][3]
                    visited.remove(j)
            visited.remove(i)
    return res
dfs(set())