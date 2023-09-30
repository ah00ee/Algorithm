import sys
import heapq

n = int(sys.stdin.readline())
hq = []
for _ in range(n):
    p, q = map(int, sys.stdin.readline().split())
    heapq.heappush(hq, (p, q))

used = [0]*100000
cnt = [0]*100000
while hq:
    tmp = heapq.heappop(hq)
    for i in range(100000):
        if used[i] <= tmp[0]:
            used[i] = tmp[1]
            cnt[i] += 1
            break
    
print(100000-cnt.count(0))
for i in cnt:
    if i == 0:
        break
    print(i, end=' ')
    