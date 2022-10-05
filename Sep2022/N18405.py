import sys
from collections import deque, defaultdict
n, k = map(int, sys.stdin.readline().split())
vir, dic = [], defaultdict(list)
for l in range(n):
    vir.append(list(map(int, sys.stdin.readline().split())))
    for m in range(n):
        if vir[l][m] != 0:
            dic[vir[l][m]].append((l, m))
s, x, y = map(int, sys.stdin.readline().split())

def bfs(deq, cnt):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False]*n for _ in range(n)]
    while cnt:
        i, j = deq.popleft()
        for p in range(4):
            nx = i+dx[p]
            ny = j+dy[p]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if not visited[nx][ny] and vir[nx][ny] == 0:
                vir[nx][ny] = vir[i][j]
                visited[nx][ny] = True
                deq.append((nx, ny))
        cnt -= 1
q, cnt = deque(), 0
for t in sorted(dic.keys()):
    for u in dic[t]:
        q.append(u)
for _ in range(s):
    bfs(q, cnt=len(q))
    if vir[x-1][y-1] != 0:
        print(vir[x-1][y-1])
        exit()
print(0)