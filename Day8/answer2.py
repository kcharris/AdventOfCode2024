f = open("Day8\data.txt")
arr = []
for line in f.readlines():
    arr.append([c for c in line.rstrip()])
m = len(arr)
n = len(arr[0])
# contains set containing node locations
d = {}
# set of tuple locations within bounds
antinodes = set()

def getAntinodes(n1, n2):
    y1, x1 = n1
    y2, x2 = n2

    yd = abs(y2 - y1)
    xd = abs(x2 - x1)
    count = 1
    res = [n1, n2]
    while True:
        a1y = None
        a1x = None
        a2y = None
        a2x = None
        if y2 < y1:
            a1y = y1 + (yd * count)
            a2y = y2 - (yd * count)
        else:
            a1y = y1 - (yd * count)
            a2y = y2 + (yd * count)
        if x2 < x1:
            a1x = x1 + (xd * count)
            a2x = x2 - (xd * count)
        else:
            a1x = x1 - (xd * count)
            a2x = x2 + (xd * count)

        flag1 = True
        flag2 = True
        if a1y < m and a1y >= 0 and a1x < n and a1x >= 0:
            res.append((a1y, a1x))
        else:
            flag1 = False
        if a2y < m and a2y >= 0 and a2x < n and a2x >= 0:
            res.append((a2y, a2x))
        else:
            flag2 = False
        if flag1 == False and flag2 == False:
            break
        count += 1
    return res

for i in range(m):
    for j in range(n):
        if arr[i][j] != ".":
            curr = arr[i][j]
            if curr in d:
                for t in d[curr]:
                    for t1 in getAntinodes((i, j), t):
                        antinodes.add(t1)
            else:
                d[curr] = set()
            d[curr].add((i, j))

print(len(antinodes))