import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
painting = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    painting.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    area = 0
    s = deque()
    s.append((x, y))
    visited[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while s:
        tmpX, tmpY = s[-1]
        flag = False
        for i in range(4):
            nx, ny = tmpX + dx[i], tmpY + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if painting[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                flag = True
                s.append((nx, ny))

        if not flag:
            s.pop()
            area += 1
    return area

cnt, maxArea = 0, 0
for i in range(n):
    for j in range(m):
        if painting[i][j] == 1 and not visited[i][j]:
            cnt += 1
            maxArea = max(maxArea, dfs(i, j))
print(cnt)
print(maxArea)