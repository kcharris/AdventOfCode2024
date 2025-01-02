import networkx as nx
from pprint import pprint
import numpy as np
f = open("Day20\data.txt")
# f = open("Day20\data1.txt")

M = 10**10
area = []
for line in f:
    area.append([c for c in line.rstrip()])
m = len(area)
n = len(area[0])

directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}
directions = ((0,1), (0,-1), (1,0), (-1, 0))
clock = {"^":">", ">":"v", "v":"<","<":"^"}
c_clock = {"^":"<", "<":"v", "v":">",">":"^"}


def withinBounds(y, x):
    if y >= 0 and y < m and x >= 0 and x < n:
        return True
    return False

# get start position
start = None
end = None
for i in range(m):
    for j in range(n):
        if area[i][j] == "S":
            start = (i, j)
        if area[i][j] == "E":
            end = (i,j)
        
# set initial path legth and a dp tab using a bfs
init_length = 0
def getDistArr(arr, start):
    tab = [[-M for _ in range(n)] for _ in range(m)]
    tab[start[0]][start[1]] = 0
    nodes = [start]
    while len(nodes):
        next_nodes = []
        while len(nodes):
            curr_node = nodes.pop()
            y, x = curr_node
            for dy, dx in directions:
                new_y = y + dy
                new_x = x + dx
                if withinBounds(new_y, new_x) and tab[new_y][new_x] == -M and arr[new_y][new_x] != "#":
                    tab[new_y][new_x] = tab[y][x] + 1
                    next_nodes.append((new_y, new_x))
        nodes = next_nodes.copy()
    return tab.copy()

start_tab = getDistArr(area, start)
end_tab = getDistArr(area, end)
init_length = end_tab[start[0]][start[1]]

cheat_sec = 20
# gather the number of new paths based on path length into a counter
costs = {}
for y in range(m):
    curr_saved = M
    for x in range(n):
        if area[y][x] == "#":
            continue
        for dy in range(-cheat_sec, cheat_sec + 1):
            for dx in range(-cheat_sec, cheat_sec+1):
                if (dy == 0 and dx == 0) or abs(dy) + abs(dx) > cheat_sec:
                    continue
                ty, tx = y +dy, x+dx
                if not withinBounds(ty, tx) or area[ty][tx] == "#":
                    continue
                # redo formula to use dist from start and dist from end
                length = start_tab[y][x] + end_tab[ty][tx] + abs(dy) + abs(dx)
                # if length-2 > 0:
                # curr_res = min(curr_res, init_length - length - 2)

                curr_saved = init_length - length
                if curr_saved > 0:
                    costs[curr_saved] = costs.setdefault(curr_saved, 0) + 1

res = 0
for k in costs:
    if k >= 100 and k != M:
        res += costs[k]
print(res)
