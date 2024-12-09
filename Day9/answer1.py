f = open("Day9\data.txt")
# f = open("Day9\data copy.txt")

s = f.read()
s = s.rstrip()
arr = []
for i in range(len(s)):
    if i % 2 == 0:
        for j in range(int(s[i])):
            arr.append(i//2)
    else:
        for j in range(int(s[i])):
            arr.append(".")

r = len(arr)-1
l = 0
while l < r:
    if arr[l] == ".":
        while l < r and arr[r] == ".":
            r -= 1
        arr[l] = arr[r]
        arr[r] = "."
        r -= 1
    l += 1

r += 1
l = 0
csum = 0
while arr[l] != "." and arr[l] != r:
    csum += l * arr[l]
    l += 1
print(csum)