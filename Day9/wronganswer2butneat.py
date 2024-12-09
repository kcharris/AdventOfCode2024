# f = open("Day9\data.txt")
f = open("Day9\data copy.txt")

s = f.read()
s = s.rstrip()
s = [int(c) for c in s]
arr = []
d = {}
for i in range(len(s)):
    if i % 2 == 0:
        for j in range(s[i]):
            arr.append(i//2)
    else:
        for j in range(s[i]):
            arr.append(".")

l = 0
while l < len(arr):
    if arr[l] == ".":
        # find the len of the "." subarray
        sub_l = l
        while l < len(arr) and arr[l] == ".":
            l += 1
        # subarray len = l - sub_l
        # next, move from the end of arr up to and including l to find potential indexes to fill with
        # numbers len can be found with r and a sub_r
        r = len(arr)-1
        sub_r = r
        while l <= r:
            if arr[r] != ".":
                sub_r = r
                # grab the subarray for r containing numbers
                while r >= l and arr[r] == arr[sub_r]:
                    r -= 1
                # if the r subarray is <= l subarray, move r array to sub_l location
                if sub_r-r <= l - sub_l:
                    for i in range(sub_r-r):
                        arr[sub_l] = arr[sub_r]
                        arr[sub_r] = "."
                        sub_r -= 1
                        sub_l += 1
            r -= 1
    l += 1

csum = 0
print(arr)
for i in range(len(arr)):
    if arr[i] != ".":
        csum += i * arr[i]
print(csum)