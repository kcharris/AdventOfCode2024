def is_safe(arr,asc, key=0):
    if len(arr) <= 1:
        return True
    res = True
    for i in range(len(arr)-1):
        if asc:
            val = arr[i+1] - arr[i]
        else:
            val = arr[i] - arr[i+1]

        if val > 3 or val < 1:
            if key == 1:
                return False
            else:
                # try removing current
                res = is_safe(arr[:i] + arr[i+1:], asc, key=1)
                # try removing next
                res |= is_safe(arr[:i+1] + arr[i+2:], asc, key=1)
                return res
    return res

# def run_tests():
#     arr1 = [41, 38, 39, 42, 45, 47, 48, 49]
#     print(is_safe(arr1, True))
# run_tests()

res = 0  
with open("Day2/data.txt") as file:
    for line in file:
        arr1 = list(map(int, line.split()))
        if is_safe(arr1, True) or is_safe(arr1, False):
            res += 1
print(res)