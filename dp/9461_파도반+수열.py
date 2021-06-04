lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(int(input())):
    n = int(input())

    if n <= len(lst):
        print(lst[n - 1])
        continue
    for i in range(len(lst), n):
        lst.append(lst[i - 1] + lst[i - 5])

    print(lst[-1])