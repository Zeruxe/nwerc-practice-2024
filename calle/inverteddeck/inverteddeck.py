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
while r < n and l < r:
    print(l, r)
    if nums[r] >= nums[l-1] and nums[l] >= nums[r+1] and nums[r+1] > nums[r]: 
        start, end = l + 1, r + 1
        flipped = True 
    if nums[l] >= nums[r]: 
        r += 1
    else:
        l, r = r, r + 1 
print(start, end)
