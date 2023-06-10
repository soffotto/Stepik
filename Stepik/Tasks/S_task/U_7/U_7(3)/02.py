# total = 0
# num = int(input('Введите число: '))
#
# for i in range(num):
#     ch = int(input('Введите число к сумме: '))
#     total += ch
# print(total)

total = 0
for i in range(int(input('Введите число: '))):
    total += int(input('Введите число к сумме: '))
print(total)