from math import gcd

n, d = input().split()
n, d = int(n), int(d)

out = input().split()

fizz = []
buzz = []

for i in range(n, d+1): 
    if out[i-n] == 'Fizz': 
        fizz.append(i)
    elif out[i-n] == 'Buzz': 
        buzz.append(i)
    elif out[i-n] == 'FizzBuzz': 
        fizz.append(i)
        buzz.append(i)

fizz_res = 0
buzz_res = 0

if len(fizz) == 0: 
    fizz_res = d+1
elif len(fizz) == 1: 
    fizz_res = fizz[0]
elif len(fizz) >= 2: 
    fizz_res = fizz[0]
    for val in fizz: 
        fizz_res = gcd(fizz_res, val)
if len(buzz) == 0: 
    buzz_res = d+1
elif len(buzz) == 1: 
    buzz_res = buzz[0]
elif len(buzz) >= 2: 
    buzz_res = buzz[0]
    for val in buzz: 
        buzz_res = gcd(buzz_res, val)
print(fizz_res, buzz_res)

