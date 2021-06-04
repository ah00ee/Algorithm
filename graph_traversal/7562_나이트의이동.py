from collections import deque
def bfs(board, x, y):
    q = deque()
    visited = [[False]*len(board[0]) for i in range(len(board[0]))]

    q.append([x, y, 0])
    visited[x][y] = True

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    while len(q) > 0:
        tmp = q.popleft()
        if board[tmp[0]][tmp[1]] == 1:
            return tmp[2]

        for i in range(8):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= len(board[0]) or ny >= len(board[0]):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny, tmp[2] + 1])
    return -1

t = int(input())
for i in range(t):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    board[end_x][end_y] = 1
    print(bfs(board, start_x, start_y))