s = []
for i in range(int(input('Введите число итераций'))):
    s.append(int(input('Введите число')))
del s[s.index(min(s))]
del s[s.index(max(s))]
print(*s, sep= '\n')
