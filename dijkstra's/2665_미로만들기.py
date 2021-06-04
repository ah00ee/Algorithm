import heapq

n = int(input())
visited = [[0]*n for _ in range(n)]
board = [list(input()) for _ in range(n)]

q = []
heapq.heappush(q, [0, 0, 0])
visited[0][0] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
    tmp = heapq.heappop(q)

    if tmp[1] == n - 1 and tmp[2] == n - 1:
        print(tmp[0])
        break

    for i in range(4):
        nx = tmp[1] + dx[i]
        ny = tmp[2] + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = 1

            if board[nx][ny] == '0':
                heapq.heappush(q, [tmp[0] + 1, nx, ny])
            else:
                heapq.heappush(q, [tmp[0], nx, ny])
            