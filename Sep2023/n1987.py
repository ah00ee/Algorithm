from collections import deque
import sys

r, c = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))

def bfs(r, c, board):
    q = deque()
    q.append((0, 0, board[0][0]))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    maximum = 1
    while q:
        tmpX, tmpY, visited = q.popleft()
        maximum = max(maximum, len(visited))

        for i in range(4):
            nx = tmpX + dx[i]
            ny = tmpY + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if board[nx][ny] not in visited:
                q.append((nx, ny, visited+board[nx][ny]))

    return maximum

print(bfs(r, c, board))