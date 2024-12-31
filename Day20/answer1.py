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
    if y >= 0 and y < m and x >= 0 and x < m:
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
    tab = [[0 for i in range(n)] for _ in range(m)]
    nodes = [start]
    while len(nodes):
        next_nodes = []
        while len(nodes):
            curr_node = nodes.pop()
            y, x = curr_node
            for dy, dx in directions:
                new_y = y + dy
                new_x = x + dx
                if withinBounds(new_y, new_x) and tab[new_y][new_x] == 0 and arr[new_y][new_x] != "#":
                    tab[new_y][new_x] = tab[y][x] + 1
                    next_nodes.append((new_y, new_x))
        nodes = next_nodes.copy()
    tab[start[0]][start[1]] = 0
    return tab.copy()

start_tab = getDistArr(area, start)
end_tab = getDistArr(area, end)
init_length = end_tab[start[0]][start[1]]

cheat_sec = 2
# gather the number of new paths based on path length into a counter
costs = {}
visited = set()
for y in range(m):
    curr_saved = M
    for x in range(n):
        if area[y][x] == "#":
            continue
        # I think the cheats are specific to walls and now I need to adjust the code to find paths through walls instead of compairing reachable tracks from any distance.
        # ???
        for mult1 in range(cheat_sec + 1):
            for mult2 in range(cheat_sec+1):
                if mult1 + mult2 == 0 or mult1 + mult2 > cheat_sec:
                    continue
                for i in range(len(directions)):
                    dy, dx = directions[i]
                    ty, tx = y +(dy*mult1), x+(dx*mult2)
                    if not withinBounds(ty, tx) or area[ty][tx] == "#":
                        continue
                    # redo formula to use dist from start and dist from end
                    length = abs(start_tab[y][x] + end_tab[ty][tx]) + (mult1 + mult2)
                    # if length-2 > 0:
                    # curr_res = min(curr_res, init_length - length - 2)

                    curr_saved = init_length - length
                    costs[curr_saved] = costs.setdefault(curr_saved, 0) + 1

res = 0
print([(k, costs[k]) for k in sorted(costs)])
for k in costs:
    if k >= 100 and k != M:
        res += costs[k]
print(res)
