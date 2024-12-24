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

# 8 wires, or 4 pairs, have been swapped and need to be found before the x and y numbers (from bit arrays) can perform addition.

def get_wires():
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
                    if d[b] != None and d[c] != None:
                        d[a] = d[b] ^ d[c]
                    if d[a] != None and d[c] != None:
                        d[b] = d[a] ^ d[c]
    if len(d.keys()) != len(found):
        return {}
    return d.copy()

bit_arr = []
for i in range(99, -1,-1):
    curr_z = "z{:02d}".format(i)
    if curr_z in d:
        bit_arr.append(d[curr_z])

print(int("0b" + "".join(map(str, bit_arr)),2))


