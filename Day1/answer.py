f = open("Day1\data.txt")
arr1 = []
arr2 = []
while True:
    s = f.readline()
    if s == "":
        break
    num1, num2 = map(int, s.split())
    arr1.append(int(num1))
    arr2.append(int(num2))

arr1.sort()
arr2.sort()
res = 0
for i in range(len(arr1)):
    res += abs(arr1[i] - arr2[i])

print(res)