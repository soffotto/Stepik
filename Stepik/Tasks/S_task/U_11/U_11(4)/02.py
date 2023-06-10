num = int(input('Введите число итераций : '))
l = []
for i in range(num):
    n = int(input('Введите число: '))
    x = n ** 2 + n * 2 + 1
    l.append(x)
print(*l, sep='\n')

