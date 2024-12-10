# f = open("Day10\data.txt")
f = open("Day10\data.txt")

arr = []
for line in f:
    arr.append([int(c) for c in line.rstrip()])

# set of visited tuples
v = set()

m = len(arr)
n = len(arr[0])
d = ((1, 0),(-1,0),(0,1),(0,-1))

def bfs(t):
    y, x = t
    if arr[y][x] == 9:
        return 1
    
    res = 0
    for yd, xd in d:
        ny = y + yd
        nx = x + xd
        if (ny < m and ny >= 0 and nx < n and nx >= 0 and arr[y][x] + 1 == arr[ny][nx] and (ny, nx) not in v):
            res += bfs((ny,nx))
    return res

res = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            res += bfs((i, j))

print(res)