n, c, b = map(int, input().split())

broken = set(map(int, input().split()))

res = list('0' * n)

for val in broken: 
    res[val-1] = '0'

if c % 2 == 0:
    res[0] = '0'
else: 
    res[0] = '1'

#count all bit changes 
count = 0
for i in range(1, len(res)): 
    if res[i] != res[i-1]: 
        count += 1 

for i in range(1, len(res)-1): 
    if count < c and i+1 not in broken and (res[i] == res[i-1] and res[i] ==res[i+1]):
        res[i] = '1' if res[i] == '0' else '0'
        count += 2
print(''.join(res))
