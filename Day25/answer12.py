from pprint import pprint
f = open("Day25\data.txt")
# f = open("Day25\data1.txt")

input_arr = f.readlines()
i = 0
keys = []
locks = []

def getColumnCount(i):
    columns = [0,0,0,0,0]
    for row in range(i, i+7):
        for col in range(5):
            if input_arr[row][col] != ".":
                columns[col] += 1
    return columns.copy()

for i in range(0, len(input_arr), 8):
    columns = getColumnCount(i)
    # handle key
    if input_arr[i][0] == "#":
        locks.append(columns)
    else:
        keys.append(columns)

print(keys)
print(locks)
res = 0
for key in keys:
    for lock in locks:
        flag = True
        for i in range(5):
            if key[i] + lock[i] >= 8:
                flag = False
        if flag == True:
            res += 1
print(res)
