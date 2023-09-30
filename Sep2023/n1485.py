import sys

t = int(sys.stdin.readline())
for _ in range(t):
    dot, dis = [], []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().split())
        dot.append((x, y))
    for i in range(0, 3):
        for j in range(i+1, 4):
            dis.append((dot[i][0]-dot[j][0])**2+(dot[i][1]-dot[j][1])**2)

    dis = set(dis)
    if len(dis) == 2 and 2*min(dis) == max(dis):
        print(1)
    else:
        print(0)