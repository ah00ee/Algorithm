import sys
from collections import deque

n = int(sys.stdin.readline())
height = []

for _ in range(n):
    height.append(list(map(int, sys.stdin.readline().split())))

def dfs(startX, startY, h):
    s = deque()
    s.append([startX, startY])
    visited[startX][startY] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while s:
        sX, sY = s.pop()

        for i in range(4):
            nx = sX + dx[i]
            ny = sY + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[nx][ny] and height[nx][ny] > h:
                visited[nx][ny] = True
                s.append([nx, ny])

maxCnt = 1
for k in range(1, 101):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if height[i][j] > k and not visited[i][j]:
                cnt += 1
                dfs(i, j, k)
    if cnt == 0:
        break
    maxCnt = max(maxCnt, cnt)

print(maxCnt)