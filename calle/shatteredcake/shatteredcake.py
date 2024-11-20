w = int(input())
n = int(input())
pcs = []
for _ in range(n): 
    pcs.append(list(map(int, input().split())))
print(int(sum([a*b for [a,b] in pcs])/w))

