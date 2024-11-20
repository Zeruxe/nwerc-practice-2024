n = int(input())

nums = list(map(int, input().split()))

if nums == sorted(nums): 
    print("1 1")
    exit()

subs = []

start, end = -1, -1
for i in range(1, n): 
    if nums[i] <= nums[i-1]: 
        if start == -1: 
            start = i-1 
            end = i 
        else: 
            end += 1 
    elif nums[i] > nums[i-1]: 
        if nums[start] != nums[end]: 
            subs.append((start, end))
        start, end = -1, -1

if nums[start] != nums[end]: 
    subs.append((start, end))
if len(subs) > 1: 
    print("impossible")
    exit()

start, end = subs[0]

nums[start:end+1] = nums[start:end+1][::-1]

if nums == sorted(nums): 
    print(start+1, end+1)
else: 
    print("impossible")
