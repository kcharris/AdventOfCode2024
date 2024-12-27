f = open("Day21\data.txt")
f = open("Day21\data.txt")

key_tab = {}
dpad_tab = {}
arr = []
for line in f:
    arr.append([c for c in line.rstrip()])

keypad = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, "A"]
]

dpad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

keypad_start = (3, 2)
dpad_start = (0, 2)

dpad_dist = [
    [0,0,0],
    [0,0,0]
]
keypad_dist = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for row in range(len(keypad)):
    for col in range(len(keypad[0])):
        k = (row, col)
        key_tab[k] = keypad_dist.copy()
        # perform a bfs on keypad recording the distance to all indexes from start at (row, col)
        # if 9 is at (2, 0), and 1 is at (0, 2), then key_tab[(2,0)][(0,2)] = 4

print(key_tab)