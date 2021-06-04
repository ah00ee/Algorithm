from collections import deque

def bfs(i, j, apt, visited):
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 1
    while len(q) > 0:
        tmp = q.pop()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if apt[nx][ny] == "1" and visited[nx][ny] == False:
                cnt += 1
                visited[nx][ny] = True
                q.append([nx, ny])
    return cnt
n = int(input())
apt = []
visited = [[False]*n for _ in range(n)]

result = []
for _ in range(n):
    apt.append(list(input()))

for i in range(n):
    for j in range(n):
        if apt[i][j] == "1":
            cnt = bfs(i, j, apt, visited)
            if cnt != 0:
                result.append(cnt)
result.sort()
print(len(result))
for i in result:
    if i != 0:
        print(i)