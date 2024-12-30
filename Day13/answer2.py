import re
f = open("Day13\data.txt")
# f = open("Day13\data1.txt")
M = 10**14 + 7
adjust = 10_000_000_000_000
arr = []
for line in f.readlines():
    l = line.rstrip()
    if l == "":
        continue
    arr.append(l)

def getCurrentVar(idx):
    p = re.compile(r"X\+(\d*), Y\+(\d*)")
    a = re.findall(p, arr[i*3])[0]
    a = list(map(int, a))
    b = re.findall(p, arr[i*3+1])[0]
    b = list(map(int, b))
    prize = re.findall(r"X=(\d*), Y=(\d*)", arr[i*3+2])[0]
    prize = list(map(int, prize))
    return (a, b, prize)

d = {}
def findMinTokens(a, b, prize):
    px, py = prize
    ax, ay = a
    bx, by = b
    ap = (px*by - py*bx) // (ax*by - ay*bx)
    bp = (ax*py - ay*px) // (ax*by - ay*bx)

    ans_x, ans_y = ax * ap + bx * bp, ay * ap + by * bp
    if (ans_x, ans_y) == tuple(prize):
        return ap * 3 + bp
    return M

res = 0
for i in range(len(arr)//3):
    d = {}
    a, b, prize = getCurrentVar(i)
    prize[0] += adjust
    prize[1] += adjust
    curr_res = findMinTokens(a, b, prize)

    res += curr_res if curr_res != M else 0
print(res)
