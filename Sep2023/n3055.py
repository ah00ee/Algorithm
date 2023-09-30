import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
forest = []
for _ in range(r):
    forest.append(list(sys.stdin.readline().strip()))

q = deque()
visited = [[False]*c for _ in range(r)]
sX, sY = 0, 0
for i in range(r):
    for j in range(c):
        if forest[i][j] == '*':
            q.append((i, j))
            visited[i][j] = True
        if forest[i][j] == 'S':
            sX, sY = i, j
            visited[i][j] = True
q.append((sX, sY))

def bfs(forest, q, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt, cntPost = len(q), 0
    sec = 0
    while q:
        tmpX, tmpY = q.popleft()
        cnt -= 1

        for i in range(4):
            nx = tmpX + dx[i]
            ny = tmpY + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if not visited[nx][ny] and forest[nx][ny] == '.':
                cntPost += 1
                q.append((nx, ny))
                visited[nx][ny] = True
                forest[nx][ny] = forest[tmpX][tmpY]
            if forest[tmpX][tmpY] == 'S' and forest[nx][ny] == 'D':
                return sec+1

        if cnt == 0:
            cnt = cntPost
            cntPost = 0
            sec += 1
    
    return "KAKTUS"

print(bfs(forest, q, visited))
