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
blinks = 75

def dfs_helper(num, depth):
    if depth == 0:
        return 1
    key = (num, depth)
    if key in dp:
        return dp[key]
    dp[key] = 0

    if num == 0:
        dp[key] += dfs_helper(1, depth-1)
    elif getLen(num) % 2 == 0:
        st_num = str(num)
        l = int(st_num[:len(st_num)//2])
        r = int(st_num[len(st_num)//2:])
        dp[key] += dfs_helper(l, depth-1)
        dp[key] += dfs_helper(r, depth-1)
    else:
        dp[key] += dfs_helper(num*2024, depth-1)

    return dp[key]

for i in range(len(stones)):
    res += dfs_helper(stones[i], blinks)

print(res)