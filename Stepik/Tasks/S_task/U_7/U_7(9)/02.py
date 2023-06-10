# 1
# 121
# 12321
# 1234321
# 123454321

num = 5



for i in range(1, num + 1):
    count = 0
    for j in range(i):
        count += 1
        print(count, end='')
    for k in range(i, 1, -1):
        count -= 1
        print(count, end='')
    print()