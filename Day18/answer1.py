import networkx as nx
from pprint import pprint
f = open("Day18\data.txt")
m = 71
# f = open("Day18\data1.txt")
# m = 7

n = m
M = 10**10
arr = []
for line in f:
    arr.append(list(map(int, line.rstrip().split(","))))

area = [[0 for _ in range(m)] for _ in range(m)]
g = nx.DiGraph()

directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}
clock = {"^":">", ">":"v", "v":"<","<":"^"}
c_clock = {"^":"<", "<":"v", "v":">",">":"^"}

def withinBounds(pos):
    y, x = pos
    if y >= 0 and y < m and x >= 0 and x < m:
        return True
    return False

def setGraph():
    g = nx.DiGraph()
    for i in range(m):
        for j in range(n):
            if area[i][j] == "#":
                    continue
            for d in directions:
                p = (i, j)
                dy, dx = directions[d]
                new_p = (i + dy, j + dx)
                if withinBounds(new_p) and area[new_p[0]][new_p[1]] != "#":
                    g.add_edge(p, new_p, weight = 1)
    return g
                
start = (0,0)
end = (m-1, m-1)

length = 0
path = 0

l = 0
r = len(arr)-1

while l < r:
    mid = l + (r-l) // 2
    area = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(mid):
        y, x = arr[i]
        area[y][x] = "#"
    g = setGraph()

    try:
        length, path = nx.single_source_dijkstra(g, start, (end[0], end[1]))
        l = mid + 1
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        a, b = arr[mid-1]
        r = mid

print(a,b)