# Напишите функцию print_digit_sum(),
# которая принимает одно целое число num
# и выводит на печать сумму его цифр.

def print_digit_sum(num,count):
    while num > 0:
        s = num % 10
        count = count + s
        num = num // 10
    print(count)

count = 0
num = int(input())

print_digit_sum(num,count)