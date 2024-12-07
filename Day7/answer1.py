f = open("Day7\data.txt")
res = 0
arr = []
for line in f.readlines():
    line = line.rstrip()
    nums = list(line.split())
    nums[0] = nums[0][:len(nums[0])-1]
    nums = list(map(int, nums))
    arr.append(nums)

def helper(i, total, target, nums):
    if i == len(nums):
        if total == target:
            return True
        else:
            return False
    res = False
    res |= helper(i+1, total + nums[i], target, nums)
    res |= helper(i+1, total * nums[i], target, nums)
    return res

for i in range(len(arr)):
    if helper(2, arr[i][1], arr[i][0], arr[i]):
        res += arr[i][0]

print(res)
        

    