n = int(input())
m = int(input())

for _ in range(n, m - 1, -1):
    if _ %2 != 0:
        print(_)
