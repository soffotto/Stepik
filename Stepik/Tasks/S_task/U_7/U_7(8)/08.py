# 10i + 5j +0.5k = 100

total = 0

for i in range(1, 11):
    for j in range(1, 21):
        for k in range(1, 201):
            if 1000 * i +  500 * j + 50 * k == 10000 and i + j + k == 100:
                total += 1
                print('i = ', i , 'j = ', j, 'k = ', k)

print(total)