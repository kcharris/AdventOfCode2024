import re
from pprint import pprint
f = open("Day24\data.txt")
f = open("Day24\data1.txt")

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

# update code to first collect all the keys and set initial values to None
# after setting values, update the values to match the initital input
#
initial_wires = {}
for s in initial:
    m = re.findall(r"([\d\w]{3}): (\d)", s)
    a, b = m[0]
    initial_wires[a] = int(b)

gate_arr = []
for s in gates:
    m = re.findall(r"([\d\w]{3}) (\w+) ([\d\w]{3}) -> ([\d\w]{3})", s)
    gate_arr.append(list(m[0]))

# 8 gate outputs, or 4 pairs, have been swapped and need to be found before the x and y numbers (from bit arrays) can perform addition.
def getWires(initial_wires, gate_arr):
    d = initial_wires.copy()
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

def wireNum(d, l):
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
    x, x_msb = wireNum(d, "x")
    y, y_msb = wireNum(d, "y")
    z, z_msb = wireNum(d, "z")
    if (x + y) % 2**(z_msb) == z:
        return True
    return False

"""
There are 4 pairs of gates whose output wires have been swapped.

How do I test every swapped pair? ultimately n**4?
n on each level.

can use dp on sorted d keys to reduce operations, might actually be possible.
"""
# while True:
#     arr_copy = arr.copy()
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             for k in range(len(arr)-1):
#                 if k != i and k != j:
#                     for h in range(k + 1, len(arr)):
#                         if h != i and h != j:
#                             get
memo = {}
# try all pairs with memo
def dfs(visited, num_pairs=4):
    if len(visited) == num_pairs:
        updated_d = getWires(initial_wires, gate_arr)
        if isValidXYZ(updated_d):
            return sorted([gate_arr[x][3] for x in visited])
        return None
    key = str(sorted(visited))
    if key in memo:
        return memo[key]
    memo[key] = None
    # n**2
    for i in range(len(gate_arr)):
        for j in range(i+1, len(gate_arr)):
            pair = (i, j)
            if pair not in visited:
                visited.add(pair)
                gate_arr[i][3], gate_arr[j][3] = gate_arr[j][3], gate_arr[i][3]
                curr = dfs(visited, num_pairs)
                if curr != None:
                    memo[key] = curr
                gate_arr[i][3], gate_arr[j][3] = gate_arr[j][3], gate_arr[i][3]
                visited.remove(pair)
    return memo[key]
print(dfs(set()))
