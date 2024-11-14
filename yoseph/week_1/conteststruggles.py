
n, k = map(int, input().split())
a, b = map(int, input().split())

temp_1 = 0
temp_2 = 0
temp_3 = 0
temp_4 = 0

temp_1 = n*a
temp_2 = k*b

temp_3 = temp_1 - temp_2

temp_4 = (temp_3/(n-k))

if temp_4 > 100 or temp_4 < 0:
    print("impossible")
else:   
   print(f"{temp_4:.10f}")