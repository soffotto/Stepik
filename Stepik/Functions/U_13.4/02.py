# def get_days(m):
#     if num == 2:
#         d = 28
#     elif num % 2 == 0:
#         d = 30
#     else:
#         d = 31
#     return d
#
# num = int(input('Введите номер месяца : '))
# print(get_days(num))

# объявление функции
def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))