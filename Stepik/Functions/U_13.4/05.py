def find_all(target, symbol):
    # return [x for x in range(len(target)) if target[x] == symbol]
    l = []
    for i in range(len(target)):
        if target[i] == symbol:
            l.append(i)
    return l


target = input('Введите строку: ')
symbol = input('Введите символ: ')
print(find_all(target, symbol))
