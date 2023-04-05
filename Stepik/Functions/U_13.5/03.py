# def get_next_prime(num):
#     return len([i for i in range(1, num + 1) if num % i == 0]) == 2
#
# num = int(input('Введите число: '))
# print(get_next_prime(num))



# num = int(input('Введите число: '))
#
# while num != 0:
#     num = num + 1
#     if len([i for i in range(1, num + 1) if num % i == 0]) == 2:
#         break
#
# print(num)

def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

# считываем данные
n = int(input('Введите число: '))

# вызываем функцию
print(get_next_prime(n))

