import sys

k = int(sys.stdin.readline())

tree = {}

building = list(map(int, sys.stdin.readline().split()))

visit = [False for _ in range(2**k-1)]

print(visit)

def t():
    parent = 0
    print(parent)
    pass

for b in building:
    left, right = 0, 0
    for i in range(b):
        print(i)
        if i == 0:
            break

exit()