n, k = input().split()
n, k = int(n), int(k)
d, s = input().split()
d, s = int(d), int(s)

total_difficulty = n * d
average_unsolved_difficulty = (total_difficulty - (k * s)) / (n - k)
if average_unsolved_difficulty <= 100 or average_unsolved_difficulty < 0:
    print(average_unsolved_difficulty)

else:
    print("impossible")
