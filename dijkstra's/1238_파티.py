import sys, heapq
from collections import defaultdict

n, m, x = map(int, sys.stdin.readline().split())
village = defaultdict(list)

def dijkstra(a):
    distance = [sys.maxsize]*n
    q = []
    heapq.heappush(q, [0, a])

    while q:
        tmp = heapq.heappop(q)
        for i in village[tmp[1]]:
            if i[0] == a:
                distance[a - 1] = 0
                continue
            if distance[i[0] - 1] > i[1] + tmp[0]:
                distance[i[0] - 1] = i[1] + tmp[0]
                heapq.heappush(q, [distance[i[0] - 1], i[0]])
    
    return distance

for _ in range(m):
    start, end, t = map(int, sys.stdin.readline().split())
    village[start].append([end, t])

ans = 0
b = dijkstra(x)
for i in range(n):
    a = dijkstra(i + 1)[x - 1]
    c = b[i]
    if ans < a + c:
        ans = a + c

print(ans)