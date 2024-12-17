import networkx as nx

f = open("Day16\data.txt")
# f = open("Day16\data1.txt")

M = 10**10
area = []
g = nx.DiGraph()
for line in f:
    area.append(line.rstrip())
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

res = M
lenght = 0
path = 0
res = (M, None)
for d in directions:
    try:
        length, path = nx.single_source_dijkstra(g, start, (end[0], end[1], d))
        if length < res[0]:
            res = (length, path)
    except nx.NetworkXNoPath:
        print(f"{d} not reachable")

print(length)



