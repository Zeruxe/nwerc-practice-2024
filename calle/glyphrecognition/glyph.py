n = int(input())

points = []
for i in range(n): 
    (x, y) = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x: (x[0]**2+x[1]**2)) 
print(points)


