n = int(input())
array = list(map(int, input().split()))

array.sort()  

min_fraction = float('inf')  

for i in range(n):
    curr_min = array[i] / (i + 1)
    if curr_min > 1:
        print("impossible")
        break
    min_fraction = min(min_fraction, curr_min)
else:  
    print(min_fraction)
