import networkx as nx
from functools import cache
f = open("Day21\data.txt")
# f = open("Day21\data1.txt")

arr = []
for line in f:
    arr.append([c for c in line.rstrip()])

keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]
number_idxs = {}
for row in range(len(keypad)):
    for col in range(len(keypad[0])):
        number_idxs[keypad[row][col]] = (row, col)

dpad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]
dir_idxs = {}
for row in range(len(dpad)):
    for col in range(len(dpad[0])):
        dir_idxs[dpad[row][col]] = (row, col)

directions = ((0,1), (1,0), (-1,0),(0,-1))
def getDirection(cell1, cell2):
    d = {(0,1):">", (1,0):"v",(-1,0):"^", (0,-1):"<"}
    return d[(cell2[0]-cell1[0]), cell2[1]-cell1[1]]

key_g = nx.DiGraph()
for row in range(len(keypad)):
    for col in range(len(keypad[0])):
        for dy, dx in directions:
            new_y, new_x = row + dy, col + dx
            if new_y < len(keypad) and new_y >= 0 and new_x < len(keypad[0]) and new_x >= 0 and keypad[new_y][new_x] != None and keypad[row][col] != None:
                key_g.add_edge((row, col),(new_y, new_x), weight=1)
d_g = nx.DiGraph()
for row in range(len(dpad)):
    for col in range(len(dpad[0])):
        for dy, dx in directions:
            new_y, new_x = row + dy, col + dx
            if new_y < len(dpad) and new_y >= 0 and new_x < len(dpad[0]) and new_x >= 0 and dpad[new_y][new_x] != None and dpad[row][col] != None:
                d_g.add_edge((row, col),(new_y, new_x), weight=1)


# instead of doing the entire code at once, I could only worry about specific chr's at any given time.
memo = {}
def pressKeys(code, count):
    k = (str(code), count)
    if k in memo:
        return memo[k]
    if count == 0:
        return len(code)
    cell = dir_idxs["A"]
    memo[k] = 0
    for c in code:
        curr_res = 10**20
        paths = nx.all_shortest_paths(d_g, cell, dir_idxs[c])
        for p in paths:
            p_to_code = []
            for i in range(1,len(p)):
                p_to_code.append(getDirection(p[i-1], p[i]))
            p_to_code.append("A")
            curr_res = min(curr_res, pressKeys(p_to_code, count-1))
            
        memo[k] += curr_res
        cell = dir_idxs[c]
    return memo[k]

res = 0
for code in arr:
    r = 0
    cell = number_idxs["A"]
    for c in code:
        curr_res = 10**20
        paths = nx.all_shortest_paths(key_g, cell, number_idxs[c])
        for p in paths:
            p_to_code = []
            for i in range(1,len(p)):
                p_to_code.append(getDirection(p[i-1], p[i]))
            p_to_code.append("A")
            curr_res = min(curr_res, pressKeys(p_to_code, 25))
            
        r += curr_res
        cell = number_idxs[c]

    res += r * int("".join(code)[:3])
print(res)