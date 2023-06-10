# word = input('Введите слово:')
# while word != 'Конец':
#     print(word)
#     word = input('Введите слово:')


text = input('Ввод слова:')
s = ''
while text != 'КОНЕЦ':
    t = text
    s = s + t +'\n'
    text = input('Ввод слова:')
print(s)