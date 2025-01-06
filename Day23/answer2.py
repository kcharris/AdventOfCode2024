import networkx as nx
from pprint import pprint
f = open("Day23\data.txt")
# f = open("Day23\data1.txt")

g = nx.Graph()
for line in f.readlines():
    a, b = line.rstrip().split(sep="-")
    g.add_edge(a, b)

d = {}
for n in g:
    d[n] = set(g[n])

memo = {}
def helper(nodes, visited):
    key = ",".join(sorted(visited))
    if key in memo:
        return key
    if len(nodes) == 0:
        return key
    memo[key] = []
    for n in nodes:
        if len(d[n] & visited) == len(visited):
            visited.add(n)
            memo[key] = max(memo[key], helper(nodes & d[n], visited), key= lambda a : len(a))
            visited.remove(n)
    return memo[key]

print(helper(set(d.keys()), set()))