num = 5321
f = True

while num > 9:
    n  = num % 10
    num = num // 10
    n_1 = num % 10
    if n > n_1:
        f = False

if f:
    print('Y')
else:
    print('N')