a = int(input('Введите число: '))
b = int(input('Введите число: '))

count = 0

for i in range(a, b):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1
print(count)

# tot = 0
# for i in range(int(input()), int(input()) + 1):
#     if str(i ** 3 % 10) in '49':
#         tot += 1
# print(tot)