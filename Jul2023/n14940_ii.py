import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
d, dCnt = [], [[0]*m for _ in range(n)]
for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y, d, v):
    q = deque()
    v[x][y] = True
    q.append([x, y])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if nx < 0 or ny < 0 or nx >= len(d) or ny >= len(d[0]):
                continue
            if not v[nx][ny] and d[nx][ny] == 1:
                v[nx][ny] = True
                dCnt[nx][ny] = dCnt[qx][qy]+1
                q.append([nx, ny])

v = [[False]*len(d[0]) for _ in range(len(d))]

for i in range(n):
    for j in range(m):
        if d[i][j] == 2:
            bfs(i, j, d, v)

for i in range(n):
    for j in range(m):
        if d[i][j] and not v[i][j]:
            print(-1, end=' ')
        else: 
            print(dCnt[i][j], end=' ')
    print()