import re
f = open("Day4\data.txt")
ws = []
for line in f.readlines():
    ws.append([c for c in line])

directions = ((1,0),(0,1),(-1,0),(0,-1),
              (1,-1),(-1,1),(1,1),(-1,-1))
search_word = "XMAS"
m = len(ws)
n = len(ws[0])
def findWord(y, x):
    res = 0
    for yd, xd in directions:
        curr_y, curr_x = y, x
        search_word_idx = 1
        while (
            curr_y + yd < m and curr_y + yd >= 0 and
            curr_x + xd < n and curr_x + xd >= 0 and
            search_word_idx < len(search_word)
        ):
            curr_y += yd
            curr_x += xd
            if ws[curr_y][curr_x] != search_word[search_word_idx]:
                break
            search_word_idx += 1
        if search_word_idx == len(search_word):
            res += 1
    return res
def findMas(r, c):
    if (
        (ws[r][c] == "M" and ws[r+2][c+2] == "S" or ws[r][c] == "S" and ws[r+2][c+2] == "M") and
        (ws[r+2][c] == "M" and ws[r][c+2] == "S" or ws[r+2][c] == "S" and ws[r][c+2] == "M") and
        ws[r+1][c+1] == "A"
        ):
        return 1
    return 0

res = 0
for r in range(m-2):
    for c in range(n-2):
        if ws[r][c] == "M" or ws[r][c] == "S":
            res += findMas(r,c)
print(res)