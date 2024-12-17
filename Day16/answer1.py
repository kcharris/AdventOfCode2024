import sys
sys.setrecursionlimit(10000)

f = open("Day16\data.txt")
f = open("Day16\data1.txt")

area = []
M = 10**10
for line in f:
    area.append([c for c in line.rstrip()])
m = len(area)
n = len(area[0])
# get start position
start = None
end = None
for i in range(m):
    for j in range(n):
        if area[i][j] == "S":
            start = (i, j)
        if area[i][j] == "E":
            end = (i,j)

directions= {"^":(-1,0),"v":(1,0), "<":(0,-1),">":(0,1)}
clock = {"^":">", ">":"v", "v":"<","<":"^"}
c_clock = {"^":"<", "<":"v", "v":">",">":"^"}

def tupleHelper(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def calcScore(tup):
    return tup[0] + tup[1] * 1000

def getNP(p, d):
    yd, xd = directions[d]
    return (p[0]+yd, p[1]+xd)

# under visted update the area with d symbols and print at E
memo = {}
visited = set()
def dfs(p, d):
    if p == end:
        return (0, 0)
    
    py, px = p
    if area[py][px] == "#" or p in visited:
        return (M, M)
    key = (p, d)
    visited.add(p)

    if key in memo:
        return memo[key]

    memo[key] = (M, M)
    # forward
    np = getNP(p, d)
    memo[key] = min(memo[key], tupleHelper((1, 0), dfs(np, d)), key = lambda a: calcScore(a))

    # left
    left = c_clock[d]
    np = getNP(p, left)
    memo[key] = min(memo[key], tupleHelper((1, 1), dfs(np, left)), key = lambda a: calcScore(a))

    # right
    right = clock[d]
    np = getNP(p, right)
    memo[key] = min(memo[key], tupleHelper((1, 1), dfs(np, right)), key = lambda a: calcScore(a))

    visited.remove(p)
    return memo[key]

res_tup = dfs(start, ">")
print(calcScore(res_tup))



