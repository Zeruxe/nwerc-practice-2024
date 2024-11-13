n = int(input())

c = list(map(int, input().split()))

c.sort()
minFrac = 2

for i in range(n): 
    if c[i] > i+1: 
        print("impossible")
        exit()
    filling = c[i]/(i+1)
    minFrac = min(filling, minFrac)

print(minFrac)
