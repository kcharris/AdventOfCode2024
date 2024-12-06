import re
f = open("Day5\data.txt")
f1 = open("Day5\data1.txt")
res = 0
g = {}

for line in f.readlines():
    x, y = map(int, line.split("|"))
    if x not in g:
        g[x] = set()
    g[x].add(y)

arr = []
for line in f1.readlines():
    arr.append(list(map(int, line.split(","))))

for row in arr:
    visited = {row[0]}
    flag = True
    for i in range(1, len(row)):
        curr = row[i]
        if curr in g:
            if len(visited & g[curr]) > 0:
                flag = False
                break
        visited.add(curr)

    if flag:
        res += row[len(row)//2]

print(res)
        

