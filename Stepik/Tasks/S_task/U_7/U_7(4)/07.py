num = int(input('Введите общую стоимость услуг: '))

# 1,5,10,25

# total = 0
#
# while num != 0 :
#     if 10 < num >= 25:
#         num = num - 25
#         total += 1
#     elif 5 < num >= 10:
#         num = num - 10
#         total += 1
#     elif 1 < num >= 5:
#         num = num - 5
#         total += 1
#     elif num < 5:
#         num = num - 1
#         total += 1
# print(total)
#
#
# num = int(input())
total = 0

while num != 0:
    if num >= 25:
        num -=25
    elif num >= 10:
        num -= 10
    elif num >= 5:
        num -= 5
    elif num >= 1:
        num -= 1
    total += 1
print(total)