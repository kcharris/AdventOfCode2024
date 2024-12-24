import re
from pprint import pprint
f = open("Day24\data.txt")
# f = open("Day24\data1.txt")

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

d = {}
for s in initial:
    m = re.findall(r"([\d\w]{3}): (\d)", s)
    a, b = m[0]
    d[a] = int(b)

arr = []
for s in gates:
    m = re.findall(r"([\d\w]{3}) (\w+) ([\d\w]{3}) -> ([\d\w]{3})", s)
    for a in m[0]:
        if a not in d:
            d[a] = None
    arr.append(m[0])
del d["OR"]
del d["AND"]
del d["XOR"]

# 8 wires, or 4 pairs, have been swapped and need to be found before the x and y numbers (from bit arrays) can perform addition.

def getWires(d):
    found = set()
    for k in d:
        if d[k] != None:
            found.add(k)
    count = 1000
    while len(d.keys()) > len(found) and count > 0:
        count -= 1
        for a, op, b, c in arr:
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
    if len(d.keys()) != len(found):
        print("???")
        return {}
    return d.copy()

def wireNum(d, l):
    bit_arr = []
    for i in range(99, -1,-1):
        key = "{}{:02d}".format(l, i)
        if key in d:
            bit_arr.append(d[key])
    return int("".join(map(str, bit_arr)),2)

def isValidXYZ(d):
    x = wireNum(d, "x")
    y = wireNum(d, "y")
    z = wireNum(d, "z")
    if x + y == z:
        return True
    return False

updated_d = getWires(d.copy())
print(wireNum(updated_d, "z"))
print(isValidXYZ(updated_d))

"""
There are 4 pairs of gates whose output wires have been swapped.

How do I test every swapped pair? ultimately n**4?
n**2 on each level.

can use dp on sorted d keys to reduce operations, might actually be possible.
"""


