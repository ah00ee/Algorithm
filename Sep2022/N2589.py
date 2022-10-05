import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
landmap, maximum = [], 0
for _ in range(n):
    landmap.append(sys.stdin.readline().strip())

def bfs(i, j, cntMax):
    d = deque()
    d.append([i, j, 0])
    visited = [[False]*m for _ in range(n)]
    visited[i][j] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while d:
        x, y, cnt = d.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if not visited[nx][ny] and landmap[nx][ny] == "L":
                d.append((nx, ny, cnt+1))
                cntMax = cnt+1 if cntMax < cnt+1 else cntMax
                visited[nx][ny] = True
    return cntMax
    
for i in range(n):
    for j in range(m):
        if landmap[i][j] == "L":
            maximum = bfs(i, j, maximum)
print(maximum)