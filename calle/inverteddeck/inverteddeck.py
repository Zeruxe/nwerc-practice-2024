n = int(input())
nums = list(map(int, input().split()))
is_sorted = True
prevLargest = -1 
for i in range(1, n):
    prevLargest = max(prevLargest, nums[i])
    if nums[i] < nums[i - 1]:
        is_sorted = False
        first_unsorted = nums.index(prevLargest)-1
        break

if is_sorted: 
    print("1 1")
    exit()

l, r = 0, 1

flipped = False
start, end = -1, -1
while r < n and l < r and r < len(nums)-1:
    if nums[r] >= nums[l-1] and nums[l] <= nums[r+1] and nums[r+1] > nums[r]: 
        start, end = l, r
        flipped = True 
    if nums[l] >= nums[r]: 
        r += 1
    else:
        l, r = r, r + 1
if not flipped: 
    print("impossible")
    exit()
nums[start:end+1] = nums[start:end+1][::-1]
is_sorted = True
for i in range(1, n):
    prevLargest = max(prevLargest, nums[i])
    if nums[i] < nums[i - 1]:
        is_sorted = False
if is_sorted: 
    print(start+1, end+1)
else: 
    print("impossible")
