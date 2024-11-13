n, m = map(int, input().split())

t = input()
s = input()

res = ['A' for _ in range(m)]
res[m-n:] = t
s, t = list(s), list(t)
for i in range(m-1, -1, -1):
    if i-n < 0: 
        break
    res[i-n] = chr((ord(s[i])-ord(res[i]))%26 +ord('a'))

print(''.join(res))
