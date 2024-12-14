import re
from pprint import pprint
from math import ceil
f = open("Day14\data.txt")
# f = open("Day14\data1.txt")

def getCurrentVar(s):
    p = re.compile(r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)")
    a = re.findall(p, s)[0]
    a = list(map(int, a))
    return a

wide = 101
tall = 103

# wide = 11
# tall = 7
area = [[0 for _ in range(wide)] for _ in range(tall)]

arr = []
seconds = 100
for line in f.readlines():
    sub = getCurrentVar(line.rstrip())
    arr.append(sub.copy())

for p1,p2, vx,vy in arr:
    np1 = (p1 + (vx * seconds) % (wide)) % (wide)
    np2 = (p2 + (vy * seconds) % (tall)) % (tall)

    area[np2][np1] += 1

def getQuadCount(rstart, rend, cstart, cend):
    res = 0
    for i in range(rstart, rend):
        for j in range(cstart, cend):
            res += area[i][j]
    return res

q1 = getQuadCount(0, tall//2, 0, wide//2)
q2 = getQuadCount(0, tall//2, ceil(wide/2), wide)
q3 = getQuadCount(ceil(tall/2), tall, 0, wide//2)
q4 = getQuadCount(ceil(tall/2), tall, ceil(wide/2), wide)

print(q1, q2, q3, q4)
print(q1*q2*q3*q4)

