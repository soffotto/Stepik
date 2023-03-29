def get_factors(num):
    l = []
    for i in range(1, num + 1):
        if num % i == 0:
            l.append(i)
    return l

num = int(input('Введите число для итерации: '))
print(get_factors(num))