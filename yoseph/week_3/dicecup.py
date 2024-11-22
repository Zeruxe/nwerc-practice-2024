# Input
a, b = map(int, input().split())

frequency = {}

for i in range(1, a + 1):
    for j in range(1, b + 1):
        total = i + j
        if total in frequency:
            frequency[total] += 1
        else:
            frequency[total] = 1

max_frequency = max(frequency.values())

most_likely_sums = [sum_value for sum_value, freq in frequency.items() if freq == max_frequency]

most_likely_sums.sort()
for sum_value in most_likely_sums:
    print(sum_value)
