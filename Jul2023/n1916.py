import sys
import heapq

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph, dis = [[] for _ in range(n+1)], [INF]*(n+1)

for _ in range(m):
    s, d, l = map(int, sys.stdin.readline().split())
    graph[s].append((d, l))

def dijkstra(start):
    q = []
    dis[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        if cost > dis[node]:
            continue
        for i_d, i_l in graph[node]:
            if cost+i_l < dis[i_d]:
                dis[i_d] = cost+i_l
                heapq.heappush(q, (dis[i_d], i_d))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(dis[end])