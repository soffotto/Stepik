n = int(input('Введите число: '))
largest = -1

for i in range(n):
    largest_2 = int(input('Введите число последовательности : '))
    if largest_2 > largest:
        largest = largest_2

print(largest)
print(largest_2)

# n = int(input())   # вводится число членов дальнейшей последовательности
# largest = n   # n идёт в начале всей последовательности и до введения следующих является наибольшим
# previous_largest = 0   # предыдущее не вводилось, примем за 0 до переприсвоения
#
# for _ in range(n):   # начинаем цикл записи остальных чисел, их сравнивания и переприсвоения
#     num = int(input())
#     if num > largest:    # если введённое число больше largest (самое первое largest = n)
#         previous_largest = largest    # прошлое самое большое становится предыдущим наибольшим
#         largest = num   # а данное введённое становится наибольшим пока не введут следующие
#     elif previous_largest < num < largest:   # если введ. числ. больше предыдущего наибольшего но меньше наибольшего
#         previous_largest = num   # оно вытесняет пред наибольшее и само становится им.
#     else:    # num < previous_largest: если введённое число меньше предыдущего наиб, ничего не изменится
#         num = num
# print(largest)
# print(previous_largest)