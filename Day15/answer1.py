from pprint import pprint
# f = open("Day15\data.txt")
f = open("Day15\data.txt")

area = []
move = []

for line in f.readlines():
    if line[0] == "#":
        area.append([c for c in line.rstrip()])
    elif line != "\n":
        move.append([c for c in line.rstrip()])

m = len(area)
n = len(area[0])

directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}

res = 0

# get start position
start = None
for i in range(m):
    for j in range(n):
        if area[i][j] == "@":
            start = (i, j)

py, px = start
# move pieces
for i in range(len(move)):
    for j in range(len(move[0])):
        d1 = move[i][j]
        yd, xd = directions[d1]
        count = 1
        while area[py + yd * count][px + xd * count] == "O":
            count += 1
        if area[py + yd*count][px + xd * count] == "#":
            continue
        # move pieces over
        area[py][px] = "."
        area[py + yd][px + xd] = "@"
        for k in range(2,count+1):
            area[py + yd * k][px + xd * k] = "O"
        py += yd
        px += xd
        
res = 0
# find geolocation of boxes and add to result
for i in range(m):
    for j in range(n):
        if area[i][j] == "O":
            res += 100 * i + j
pprint(area)
print(res)