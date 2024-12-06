import re
f = open("Day5\data.txt")
f1 = open("Day5\data1.txt")
res = 0
g = {}

for line in f.readlines():
    x, y = map(int, line.split("|"))
    if x not in g:
        g[x] = set()
    g[x].add(y)

arr = []
for line in f1.readlines():
    arr.append(list(map(int, line.split(","))))

def is_valid(row):
    visited = {row[0]}
    flag = True
    for i in range(1, len(row)):
        curr = row[i]
        if curr in g:
            if len(visited & g[curr]) > 0:
                flag = False
                break
        visited.add(curr)
    return flag

def find_valid(row):
    # create a counter to hold the "set" containing all the numbers the current number cannot be
    # this set will be updated as the program continues, removing the "set" from the graph of the current number
    total_arr = [0 for _ in range(100)]
    for i in range(len(row)):
        if row[i] in g:
            for v in g[row[i]]:
                total_arr[v] += 1

    # bigO = 100 * (up to 20) * (up to 20)
    # then * 200 on the outside = (10**6 * 8)
    res = []
    row_set = set(row)   # luckily I didn't run into the issue where there could be duplicates 
    while len(row_set):
        # move through each possible number
        for i in range(len(total_arr)):
            # find the possible number that is in row_set, but not flagged in total_arr by it's counter
            if i in row_set and total_arr[i] < 1:
                res.append(i)
                row_set.remove(i)
                # remove the graph of the current num from the counter
                for v in g[i]:
                    total_arr[v] -= 1
    return res

print(len(arr))
count = 0
for row in arr:
    count += 1
    flag = is_valid(row)
    
    if not flag:
        new_row = find_valid(row)
        res += new_row[len(new_row)//2]

print(res)
        

