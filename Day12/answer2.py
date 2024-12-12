from pprint import pprint
f = open("Day12\data.txt")
# f = open("Day12\data1.txt")

#price = area * per for each fenced area

# given an outside perimeter, the additional perimeter contains the perimeter of immediate inside items.
# or, the perimeter is a place where "R" does not touch "R"
arr = []
for line in f:
    arr.append([c for c in line.rstrip()])
m = len(arr)
n = len(arr[0])
d = ((1,0),(0,1),(-1,0),(0,-1))

visited = set()
side_d = {}
def addToSideDict(d, p):
    yd, xd = d
    y, x = p
    if (yd, xd) not in side_d:
        side_d[(yd,xd)] = {}
    curr_d = side_d[(yd,xd)]
    # handle horizontal side
    if yd != 0:
        if y not in curr_d:
            curr_d[y] = []
        curr_d[y].append(x)
    # handle vertical side
    if xd != 0:
        if x not in curr_d:
            curr_d[x] = []
        curr_d[x].append(y)

def findSideCount():
    res = 0
    for yd, xd in d:
        curr_d = side_d[(yd, xd)]
        for k in curr_d:
            if len(curr_d[k]) == 1:
                res += 1
            else:
                sorted_v = sorted(curr_d[k])
                for i in range(len(sorted_v)-1):
                    if sorted_v[i] + 1 != sorted_v[i+1]:
                        res += 1
                if sorted_v[-1] != sorted_v[-2]:
                    res += 1
    return res

def helper(y, x, l):
    res = 1
    for yd, xd in d:
        ny = y + yd
        nx = x + xd
        if ny < m and ny >= 0 and nx < n and nx >= 0:
            if arr[ny][nx] != l:
                addToSideDict((yd, xd), (y, x))
                
            elif (ny, nx) not in visited:
                visited.add((ny, nx))
                res += helper(ny, nx, l)                
        else:
            addToSideDict((yd, xd), (y, x))
    return res

res = 0
for i in range(m):
    for j in range(n):
        if (i, j) not in visited:
            sides = set()
            side_d = {}
            visited.add((i,j))
            area = helper(i, j, arr[i][j])
            perimeter = findSideCount()
            res += area * perimeter

print(res)