from pprint import pprint
# f = open("Day15\data.txt")
f = open("Day15\data.txt")
directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}
res = 0

area = []
move = []

for line in f.readlines():
    if line[0] == "#":
        area.append([c for c in line.rstrip()])
    elif line != "\n":
        move.append([c for c in line.rstrip()])
m = len(area)
n = len(area[0])

new_arr = []
# double the area
for i in range(m):
    new_arr.append([])
    for j in range(n):
        if area[i][j] == "#":
            new_arr[i].extend(["#", "#"])
        if area[i][j] == "O":
            new_arr[i].extend(["[", "]"])
        if area[i][j] == ".":
            new_arr[i].extend([".", "."])
        if area[i][j] == "@":
            new_arr[i].extend(["@", "."])

area = new_arr.copy()
m = len(area)
n = len(area[0])
# get start position
start = None
for i in range(m):
    for j in range(n):
        if area[i][j] == "@":
            start = (i, j)

def moveA(py, px, d):
    res = True
    yd, xd = directions[d]
    npy = py + yd
    npx = px + xd

    if area[npy][npx] == "#":
        return False
    elif area[npy][npx] == "]":
        res = movePieces(npy, npx,d)
    elif area[npy][npx] == "[":
        # +1 to move to right no matter what
        res = movePieces(npy, npx+1,d)
        
    if res == False:
        return False
    
    return res

boxes = set()
# Attempts to move the player piece and moveable boxes in the way.
# Returns true if pieces were moved
def movePieces(py, px, d):
    res = True
    yd, xd = directions[d]
    npy = py + yd
    npx = px + xd

    # find "]" above current "]"
    if area[npy][npx] == "#" or area[npy][npx-1] == "#":
        return False
    # if checking left, have to check over 2 spaces, need to add one more
    elif xd == -1 and area[npy][npx+xd] == "]":
        res &= movePieces(npy, npx-1,d)
    # This moves to the correct position in up, down, and right scenarios
    elif xd != -1 and area[npy][npx] == "[":
        res &= movePieces(npy, npx+1,d)
        # find "]" above or below current "["
        if yd != 0 and area[npy][npx-1] == "]":
            res &= movePieces(npy, npx-1,d)
    # this checks for valid moves up and down
    elif xd != -1 and area[npy][npx] == "]":
        res &= movePieces(npy, npx,d)
    elif xd == 0 and area[npy][npx-1] == "]":
        res &= movePieces(npy, npx-1,d)
    
    # check for earlier failure
    if res == False:
        return res
    boxes.add((py, px))
    return res
    
    # move pieces over, I don't need to know previous, just need to move self forward
    # handle left
def moveBoxes(boxes, yd, xd):
    for py, px in boxes:
        if xd == -1:
            area[py][px] = "."
        elif xd == 1:
            area[py][px-1] = "."
        elif yd == -1:
            area[py][px] = "."
            area[py][px-1] = "."
        elif yd == 1:
            area[py][px] = "."
            area[py][px-1] = "."
    for py, px in boxes:
        npy = py + yd
        npx = px + xd
        if xd == -1:
            area[py][npx] = "]"
            area[py][npx-1] = "["
        elif xd == 1:
            area[py][npx] = "]"
            area[py][px] = "["
        elif yd == -1:
            area[npy][px] = "]"
            area[npy][px-1] = "["
        elif yd == 1:
            area[npy][px] = "]"
            area[npy][px-1] = "["

py, px = start
# move pieces
for i in range(len(move)):
    for j in range(len(move[0])):
        d1 = move[i][j]
        boxes = set()
        can_move = moveA(py,px,d1)
        if can_move:
            yd, xd = directions[d1]
            moveBoxes(boxes, yd, xd)
            area[py+yd][px+xd] = "@"
            area[py][px] = "."
            py+=yd
            px+=xd
  
res = 0
# find geolocation of boxes and add to result
for i in range(m):
    for j in range(n):
        if area[i][j] == "[":
            res += 100 * i + j
print(res)