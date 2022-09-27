import sys
t = int(sys.stdin.readline())
for _ in range(t):
    b, d = map(int, sys.stdin.readline().split())
    if b == 2:
        print(int(bin(d)[2:])%1)
    elif b == 8:
        print(int(oct(d)[2:])%7)
    elif b == 10:
        print(d%9)
    else:
        print("?")
