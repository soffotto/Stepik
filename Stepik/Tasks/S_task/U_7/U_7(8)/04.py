
# num = 9
num = int(input())

for i in range(1, num + 1):
    if i > num - i + 1:
        i = num - i + 1
    for j in range(i):
        print('*', end='')
    print('ggg')

# num = int(input())
#
# center = num // 2 + 1
# count = 0
#
# for i in range(1, num + 1):
#     if i > center:
#         count -= 1
#     else:
#         count += 1
#     for j in range(count):
#         print('*', end='')
#     print()