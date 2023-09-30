import sys
from collections import deque, defaultdict

n, k = map(int, sys.stdin.readline().split())
lab, virus = [], defaultdict(list)
visited = [[False]*n for _ in range(n)]

for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())

for i in range(n):
    for j in range(n):
        if lab[i][j] != 0:
            virus[lab[i][j]].append((i, j))
            visited[i][j] = True

def bfs(lab, n, visited, q, s):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt, cntPost = len(q), 0
    sec = s
    while q:
        tmpX, tmpY = q.popleft()
        cnt -= 1

        for i in range(4):
            nx = tmpX + dx[i]
            ny = tmpY + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny] and lab[nx][ny] == 0:
                q.append((nx, ny))
                cntPost += 1
                visited[nx][ny] = True
                lab[nx][ny] = lab[tmpX][tmpY]
        if cnt == 0:
            cnt = cntPost
            cntPost = 0
            sec -= 1
        if sec == 0:
            break

q = deque()

for key in sorted(virus.keys()):
    for val in virus[key]:
        q.append(val)
    
bfs(lab, n, visited, q, s)
print(lab[x-1][y-1])