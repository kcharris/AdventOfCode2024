import re
from pprint import pprint
from math import ceil
import matplotlib.pyplot as plt
import numpy as np
f = open("Day14\data.txt")
# f = open("Day14\data1.txt")
plt.style.use('_mpl-gallery-nogrid')

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

maxSecond = 0
maxX = 0
for seconds in range(5000, 10000, 100):
    fig = plt.figure(figsize=(10, 10))
    offset = 0
    for i in range(offset, 100 + offset):
        area = [[0 for _ in range(wide)] for _ in range(tall)]
        counter = {}
        for p1,p2, vx,vy in arr:
            np1 = (p1 + (vx * (seconds +i)) % (wide)) % (wide)
            np2 = (p2 + (vy * (seconds +i)) % (tall)) % (tall)
            key = np2

            area[np2][np1] = 1
        plt.subplot(10,10, i+1-offset)
        plt.imshow(area, cmap="grey")
        plt.axis("off")
        plt.title(str(seconds + i))

    plt.show()
print(maxSecond)
print(maxX)