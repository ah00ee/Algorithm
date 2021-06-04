n = int(input())
lst = []

if n == 0:
    print(0)
    exit()

lst.append(0)
lst.append(1)

for i in range(2, n + 1):
    lst.append(lst[i - 2] + lst[i - 1])

print(lst[-1])