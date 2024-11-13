visited = {i / 2: False for i in range(-180, 180)}

print(visited)

n = int(input())

flights = []

for i in range(n):
    flight = list(map(int, input().split()))
    flights.append(flight)

for i in range(1, len(flights)):
    flights[i - 1][1] += 180
    flights[i][1] += 180

