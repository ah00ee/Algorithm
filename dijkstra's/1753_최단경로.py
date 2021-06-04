import sys, heapq
from collections import defaultdict

in_v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
inf = sys.maxsize

d = defaultdict(list)
loc, q = [inf]*in_v, []
loc[k - 1] = 0

heapq.heappush(q, [0, k])
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    d[u].append([v, w])

while q:
    tmp = heapq.heappop(q)

    for i in d[tmp[1]]:
        num, dis = i[0] - 1, i[1]
        if loc[num] > dis + tmp[0]:
            loc[num] = dis + tmp[0]
            heapq.heappush(q, [loc[num], num + 1])

for i in loc:
    print(i if i != inf else "INF")