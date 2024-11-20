n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = [0, 0, 0]

for i in range(n): 
    for j in range(n): 
        res[(i+j+2) % 3] += a[j]*b[i]
r, b, g = res

print(r, b, g)
