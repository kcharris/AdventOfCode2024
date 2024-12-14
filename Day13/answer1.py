import re
f = open("Day13\data1.txt")
# f = open("Day13\data.txt")
M = 10**14 + 7
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

a = None
b = None
prize = None
d = {}
def findMinTokens(num):
    curr_res = M
    for ap in range(101):
        for bp in range(101):
            x = ap * a[0] + bp * b[0]
            y = ap * a[1] + bp * b[1]
            if [x, y] == prize:
                curr_res = min(curr_res, ap * 3 + bp)
    return curr_res

res = 0
for i in range(len(arr)//3):
    d = {}
    a, b, prize = getCurrentVar(i)
    prize[0] += 10_000_000_000_000
    prize[1] += 10_000_000_000_000
    curr_res = M
    tab = [0 for _ in range(1001)]
    for j in range(1001):
        tab[j] = findMinTokens(j)
    print(tab[100], tab[1000])

    # res += curr_res if curr_res != M else 0
print(res)


