f = open("Day21\data.txt")
f = open("Day21\data.txt")

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