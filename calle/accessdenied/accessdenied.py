import sys

test_string = 'A'

while True: 
    print(test_string, flush=True)
    ans = input()
    if ans == "ACCESS GRANTED":
        exit()
    time = int(ans.split()[2][1:])
    if time == 5: 
        test_string += 'A'
    else:
        wrong_pos = time // 9 - 1
        c = test_string[wrong_pos]
        if c == 'z':
            c = '0'
        elif c == 'Z': 
            c = 'a'
        else: 
            c = chr(ord(c)+1)
        test_list = list(test_string)
        test_list[wrong_pos] = c
        test_string = ''.join(test_list)

