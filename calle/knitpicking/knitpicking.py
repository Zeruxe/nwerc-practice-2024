n = int(input())

socks = []
total_socks = 0
for i in range(n): 
    curr = input().split()
    curr[2] = int(curr[2])
    socks.append(curr)
    total_socks += curr[2]

socks.sort(key= lambda x: -x[2])

res = 0

kinds = {}
for [kind, foot, num] in socks: 
    if foot != 'any': 
        if not kinds.get(kind):
            res += num
            kinds[kind] = foot

for [kind, foot, num] in socks: 
    if foot == 'any':
        if not kinds.get(kind): 
            res += 1
            break

if res == total_socks: 
    print("impossible")
else:
    print(res+1)
