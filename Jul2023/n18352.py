import sys
import heapq

INF = int(1e9)

n, m, k, x = map(int, sys.stdin.readline().split())
graph, dis = [[] for _ in range(n+1)], [INF]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    dis[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        distance, node = heapq.heappop(q)
        for i in graph[node]:
            if distance+1 < dis[i]:
                dis[i] = distance+1
                heapq.heappush(q, (dis[i], i))

dijkstra(x)

if k in dis:
    for i in range(1, n+1):
        if dis[i] == k:
            print(i)
else:
    print(-1)