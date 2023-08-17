import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = []
for _ in range(n):
    pokemon.append(sys.stdin.readline().strip())

for _ in range(m):
    p = sys.stdin.readline().strip()
    if p.isdigit():
        print(pokemon[int(p)-1])
    else:
        print(pokemon.index(p)+1)
