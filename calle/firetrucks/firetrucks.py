import sys

from collections import deque
n = int(input())

# reads the first half of the graph:
# connections from people to numbers
g = {}
for i in range(n):
    _, *cs = map(int, input().split())
    g[-(i+1)] = set(cs)

# adds the second half to the graph:
# connections from numbers to people
count = 0
ks = list(g.keys())
for k in ks:
    count += 1 
    for i in g[k]:
        curr = g.get(i, set())
        curr.add(k)
        g[i] = curr


# People are represented by negative numbers.
# Numbers are rerepsented by positives.
queue = deque([[-1, 0, 0]])
visited = set()
first_visit = set()
res = []
while queue:
    curr, prev_person, prev_val = queue.popleft()
    neighbors = g.get(curr, [])
    if curr < 0 and curr not in first_visit:
        if prev_person != 0: 
            res.append([-curr, -prev_person, prev_val])
    first_visit.add(curr)
    for val in neighbors:
        if val in visited: 
            continue
        if curr < 0: 
            queue.append([val, curr, prev_val])
            visited.add(val)
        else: 
            queue.append([val, prev_person, curr])
            visited.add(val)

if len(res) < n-1: 
    print("impossible")
    exit()

for [a, b, c] in res: 
    print(a, b, c)
