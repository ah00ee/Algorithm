from collections import deque
def bfs(n, k, visited):
    q = deque()
    q.append([n, 0])
    check = False
    while len(q) > 0:
        tmp = q.popleft()
        visited[tmp[0]] = True
        dx = [tmp[0] + 1, tmp[0] - 1, tmp[0]*2]
        for i in dx:
            if i <= 0 or i > 100000:
                continue
            if visited[i] == False:
                q.append([i, tmp[1] + 1])
                visited[i] = True
            if i == k:
                check = True
                print(q.pop()[1])
                break
        if check:
            break    

n, k = map(int, input().split())
visited = [False]*100001

if k <= n:
    print(n - k)
    exit()
bfs(n, k, visited)