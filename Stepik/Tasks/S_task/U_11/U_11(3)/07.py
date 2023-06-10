num = int(input('Введите число : '))
l = []

for i in range(num):
    l.append(i)
del l[::2]
print(l)
