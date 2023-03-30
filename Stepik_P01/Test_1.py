# number = int(input('Введите число : '))
# if number % 2 == 0:
#     print('Это число четное. ')
# else:
#     print('Это число нечетное.')

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(int(input('Введите числo:'))))

# number = int(input('Введите число : '))
# if is_even(number):
#     print('Это число четное. ')
# else:
#     print('Это число нечетное. ')