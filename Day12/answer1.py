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

def helper(y, x, l):
    s = 0
    a = 1
    res = [a, p]
    for yd, xd in d:
        ny = y + yd
        nx = x + xd
        if ny < m and ny >= 0 and nx < n and nx >= 0:
            if arr[ny][nx] != l:
                res[1] += 1
            elif (ny, nx) not in visited:
                visited.add((ny, nx))
                curr_res = helper(ny, nx, l, sides)
                res[0] += curr_res[0]
                res[1] += curr_res[1]
        else:
            res[1] += 1
    return res

res = 0
for i in range(m):
    for j in range(n):
        if (i, j) not in visited:
            sides = set()
            visited.add((i,j))
            curr = helper(i, j, arr[i][j], sides)
            res += curr[0] * curr[1]

print(res)