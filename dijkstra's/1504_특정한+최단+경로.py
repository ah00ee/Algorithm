import sys, heapq
from collections import defaultdict

n, e = map(int, sys.stdin.readline().split())
g = defaultdict(list)

def dijkstra(a):
    q, loc = [], [sys.maxsize]*n
    heapq.heappush(q, [0, a])
    loc[a - 1] = 0
        
    while q:
        dis, tmp = heapq.heappop(q)

        for i in g[tmp]:
            if loc[i[0] - 1] > i[1] + dis:
                loc[i[0] - 1] = i[1] + dis
                heapq.heappush(q, [i[1] + dis, i[0]])
    print(loc)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c])
    g[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())
visited = [False for _ in range(n)]


print(g)
for i in range(n):
    dijkstra(i + 1)