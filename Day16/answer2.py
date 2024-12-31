import networkx as nx
from pprint import pprint

f = open("Day16\data.txt")
# f = open("Day16\data1.txt")
# f = open("Day16\data2.txt")

M = 10**10
area = []
g = nx.DiGraph()
for line in f:
    area.append([c for c in line.rstrip()])
m = len(area)
n = len(area[0])

directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}
clock = {"^":">", ">":"v", "v":"<","<":"^"}
c_clock = {"^":"<", "<":"v", "v":">",">":"^"}

def tupleHelper(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def withinBounds(pos):
    y, x, _ = pos
    if y >= 0 and y < m and x >= 0 and x < n:
        return True
    return False
# get start position
start = None
end = None
for i in range(m):
    for j in range(n):
        if area[i][j] == "#":
                continue
        for d in directions:
            p = (i, j, d)
            dy, dx = directions[d]
            new_p = (i + dy, j + dx, d)
            if withinBounds(new_p) and area[new_p[0]][new_p[1]] != "#":
                g.add_edge(p, new_p, weight = 1)

            right = clock[d]
            dy, dx = directions[right]
            new_p = (i + dy, j + dx, right)
            if withinBounds(new_p) and area[new_p[0]][new_p[1]] != "#":
                g.add_edge(p, new_p, weight=1001)
                
            left = c_clock[d]
            dy, dx = directions[left]
            new_p = (i + dy, j + dx, left)
            if withinBounds(new_p) and area[new_p[0]][new_p[1]] != "#":
                g.add_edge(p, new_p, weight=1001)
                
        if area[i][j] == "S":
            start = (i, j, ">")
        if area[i][j] == "E":
            end = (i,j)

length = 0
path = 0
res = (M, None)
for d in directions:
    try:
        length, path = nx.single_source_dijkstra(g, start, (end[0], end[1], d))
        if length < res[0]:
            res = (length, d)
    except nx.NetworkXNoPath:
        print(f"{d} not reachable")

path_set = set()
paths = nx.all_shortest_paths(g, start, (end[0], end[1], res[1]), weight="weight")
paths = [p for p in paths]
for p in paths:
    for cell in p:
        path_set.add((cell[0], cell[1]))
    
print(len(path_set))




