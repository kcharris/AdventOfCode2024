import networkx as nx
f = open("Day23\data.txt")
f = open("Day23\data1.txt")

g = nx.Graph()
for line in f.readlines():
    a, b = line.rstrip().split(sep="-")
    g.add_edge(a, b)

res = 0
visited = set()
for n in g.nodes():
    for n2 in g.neighbors(n):
        for n3 in g.neighbors(n2):
            if n3 in g[n] and n in g[n3] and n2 in g[n]:
                curr_node = tuple(sorted([n,n2,n3]))
                if curr_node not in visited:
                    visited.add(curr_node)
                    if n[0] == "t" or n2[0] == "t" or n3[0] == "t":
                        res += 1

print(res)
