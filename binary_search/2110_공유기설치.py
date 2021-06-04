n, c = map(int, input().split())
loc = []
for _ in range(n):
    loc.append(int(input()))

pl = [loc[0], loc[-1]]
left, right = 0, len(loc) - 1
mid = (left + right)//2
while left <= right:
    mid = (left + right)//2
    if (mid - left) > (right - mid):
        right = mid - 1
    elif (mid - left) < (right - mid):
        left = mid + 1
    else:
        