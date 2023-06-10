# num = int(input('Введите число: '))
#
# for i in range(1, num + 1):
#     for j in range(i):
#         print(j + i , end=' ')
#     print()

num = 7
count = 0

for i in range(1, num + 1):
    for j in range(i):
        count += 1
        print(count, end=' ')
    print()