from pprint import pprint
f = open("Day25\data.txt")
# f = open("Day25\data1.txt")

input_arr = f.readlines()
i = 0
d = {}
keys = []

def getColumnCount(i):
    columns = [0,0,0,0,0]
    for row in range(i, i+7):
        for col in range(5):
            if input_arr[row][col] != ".":
                columns[col] += 1
    return columns.copy()

def addLocksToDict(columns, d, idx = 4, new_cols= []):
    if idx == -1:
        tup_col = tuple(new_cols)
        d[tup_col] = d.setdefault(tup_col, 0) + 1
        return
    for i in range(columns[len(columns) - 1 - idx] + 1):
        new_cols.append(i)
        addLocksToDict(columns, d, idx - 1, new_cols)
        new_cols.pop()

for i in range(0, len(input_arr), 8):
    columns = getColumnCount(i)
    # handle key
    if input_arr[i][0] == "#":
        addLocksToDict(columns, d)
    else:
        keys.append(columns)
    
res = 0
for key in keys:
    lock_needed = []
    for i in range(len(key)):
        lock_needed.append(5-key[i])
    tup_needed = tuple(lock_needed)
    if tup_needed in d:
        res += d[tup_needed]
print(res)
