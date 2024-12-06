from collections import defaultdict
f = open("Day1\data.txt")
arr1 = []
d2 = defaultdict(lambda : 0)
while True:
    s = f.readline()
    if s == "":
        break
    num1, num2 = map(int, s.split())
    arr1.append(num1)
    d2[num2] += 1

res = 0
for num in arr1:
    res += num * d2[num]
print(res)