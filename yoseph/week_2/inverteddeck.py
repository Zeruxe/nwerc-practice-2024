n = int(input())
v = list(map(int, input().split()))  

sorted_v = sorted(v)

left, right = 0, n - 1

while left < n and v[left] == sorted_v[left]:
    left += 1
while right > left and v[right] == sorted_v[right]:
    right -= 1

if left >= right:
    print("1 1")
else:
    v[left:right + 1] = v[left:right + 1][::-1]
    if v == sorted_v:
        print(left + 1, right + 1)  
    else:
        print("impossible")


"""n = int(input())
v = input().split()

sorted_v = sorted(v)

def reverse_sublist(list, start, end):
    list[start:end] = list[start:end][::-1]
    return list

found = False
for i in range(n):
    for j in range(i + 1, n + 1):
        v_copy = v[:]  
        reverse_sublist(v_copy, i, j)  
        if v_copy == sorted_v:
            found = True
            print(i + 1, j)
            break
    if found:
        break

if not found:
    print("impossible")
"""