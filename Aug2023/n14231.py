import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
cnt = [1]*n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            cnt[i] = max(cnt[i], cnt[j]+1)
print(max(cnt))