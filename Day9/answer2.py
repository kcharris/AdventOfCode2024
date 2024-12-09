f = open("Day9\data.txt")
# f = open("Day9\data copy.txt")

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

r = len(arr)-1
visited = set()
while r >= 0:
    if arr[r] != ".":
        # find the len of the "#" subarray
        sub_r = r
        while r >= 0 and arr[r] == arr[sub_r]:
            r -= 1
        # subarray len = sub_r - r
        # next, move from the star of the array to r attempting to find a "." window of size needed
        # numbers len can be found with r and a sub_r
        l = 0
        sub_l = 0
        while l <= r:
            if arr[l] == ".":
                sub_l = l
                # grab the subarray for l containing '.'
                while r >= l and arr[l] == arr[sub_l]:
                    l += 1
                # if the l subarray is >= r subarray, move r array to sub_l location
                if sub_r-r <= l - sub_l:
                    for i in range(sub_r-r):
                        arr[sub_l] = arr[sub_r]
                        arr[sub_r] = "."
                        sub_r -= 1
                        sub_l += 1
            l += 1
        r += 1
    r -= 1

csum = 0
for i in range(len(arr)):
    if arr[i] != ".":
        csum += i * arr[i]
print(csum)