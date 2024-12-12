f = open("Day11\data.txt")
# f = open("Day11\data1.txt")

stones = []
line = f.readline()
stones = [int(x) for x in line.rstrip().split()]

def getLen(n):
    res = 0
    while n > 0:
        res += 1
        n //= 10
    return res

dp = {}
res = 0
blinks = 25
for i in range(blinks):
    new_stones = []
    for j in range(len(stones)):
        if stones[j] == 0:
            new_stones.append(1)
        elif getLen(stones[j]) % 2 == 0:
            st = str(stones[j])
            l = int(st[:len(st)//2])
            r = int(st[len(st)//2:])
            new_stones.append(l)
            new_stones.append(r)
        else:
            new_stones.append(stones[j] * 2024)
    stones = new_stones.copy()

print(len(stones))