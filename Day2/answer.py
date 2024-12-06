safe_reports = 0

def is_safe(arr):
    if len(arr) == 1:
        return True
    for i in range(len(arr)-1):
        if arr[0] < arr[1]:
            val = arr[i+1] - arr[i]
        else:
            val = arr[i] - arr[i+1]
        if val > 3 or val < 1:
            return False
    return True

res = 0  
with open("Day2/data.txt") as file:
    for line in file:
        arr = list(map(int, line.split()))
        if is_safe(arr):
            res += 1
print(res)