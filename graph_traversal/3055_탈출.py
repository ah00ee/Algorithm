from collections import deque
r, c = map(int, input().split())
board = []
n, m = -1, -1
dots = []
start, end = -1, -1
q = deque()
visit = [[False]*c for _ in range(r)]
visited = [[False]*c for _ in range(r)]
visited[n][m] = True
for i in range(r):
    lst = list(input())
    board.append(lst)
    for j in range(c):
        if board[i][j] == '*':
            dots.append([i, j])
            q.append([i, j])
            visit[i][j] = True
        elif board[i][j] == 'S':
            n, m = i, j
        elif board[i][j] == 'D':
            start, end = i, j

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

chk = []
for i in range(4):
    st, ed = start + dx[i], end + dy[i]
    if st < 0 or ed < 0 or st >= r or ed >= c:
        continue
    chk.append([st, ed])  

def bfs_water(board, x, y, visit):
    cnt = len(q)
    while q:
        if cnt == 0:
            break
        tmp = q.popleft()
        cnt -= 1
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if board[nx][ny] == '.' and visit[nx][ny] == False:
                visit[nx][ny] = True
                board[nx][ny] = '*'
                q.append([nx, ny])
    return board

def bfs(board, n, m, visited):
    s_q = deque()
    s_q.append([n, m])
    cnt = 1
    tmpC = len(s_q)
    flag = False
    cp = False
    result = False
    
    while s_q:   
        if tmpC == 0:
            tmpC = len(s_q)
            if flag:
                cnt += 1
        tmp = s_q.popleft()
        tmpC -= 1
        for dot in dots:
            board = bfs_water(board, dot[0], dot[1], visit)

        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if board[nx][ny] == 'D':
                cp = True
                break
            
            if board[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                board[tmp[0]][tmp[1]] = '.'
                board[nx][ny] = 'S'
                flag = True
                s_q.append([nx, ny])

        if cp:
            print(cnt)
            result = True
            break
        
    if not result:
        print("KAKTUS")

bfs(board, n, m, visited)