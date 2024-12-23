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

d = {}
res = 0
for num in arr:
    prev_d = num % 10
    curr_arr = []
    curr_d = {}
    for i in range(2000):
        num = process(num)
        change = num % 10 - prev_d
        prev_d = num % 10
        curr_arr.append(change)
        if len(curr_arr) == 4:
            tup_a = tuple(curr_arr)
            if tup_a not in curr_d:
                curr_d[tup_a] = prev_d
            curr_arr.pop(0)
    for k in curr_d:
        d[k] = d.setdefault(k, 0) + curr_d[k]

print(max(d.values()))

