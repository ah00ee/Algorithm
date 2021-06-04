import sys
n = int(sys.stdin.readline())

for i in range(n):
    print(f'Case #{i+1}: ', end='')
    lst = list(sys.stdin.readline().split())
    while lst:
        print(lst.pop(), end=' ')
    print()