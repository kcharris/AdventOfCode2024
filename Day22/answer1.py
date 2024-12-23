f = open("Day22\data.txt")
# f = open("Day22\data1.txt")

arr = []

for line in f.readlines():
    arr.append(int(line.rstrip()))

def process(secret):
    by_64 = secret * 64
    secret = mixAndPrune(secret, by_64)
    by_32 = secret // 32
    secret = mixAndPrune(secret, by_32)
    by_2048 = secret * 2048
    secret = mixAndPrune(secret, by_2048)
    return secret

def mixAndPrune(secret, num):
    return (secret ^ num) % 16777216

res = 0

for num in arr:
    for i in range(2000):
        num = process(num)
    res += num

print(res)

