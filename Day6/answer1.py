f = open("Day6\data.txt")
res = 0
arr = []
for line in f.readlines():
    arr.append([c for c in line.rstrip()])

m = len(arr)
n = len(arr[0])

directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}
next_p = {"^":">", ">":"v", "v":"<","<":"^"}

# get starting position and piece
start = None
p = None
for i in range(m):
    for j in range(n):
        if arr[i][j] in directions:
            start = (i, j)
            p = arr[i][j]

# Trace a path to the end
y, x = start
while y < m and y >= 0 and x < n and x >= 0:
    arr[y][x] = "X"
    yd, xd = directions[p]
    # check for "#"
    while (y + yd < m and y + yd >= 0 and x + xd < n and x + xd >= 0 and arr[y+yd][x+xd] == "#"):
        p = next_p[p]
        yd, xd = directions[p]
    y += yd
    x += xd

# Total the found x's
for i in range(m):
    for j in range(n):
        if arr[i][j] == "X":
            res += 1

print(res)
        
        
        