num_popul = 10
num_sum = 50
num_day = 6

for i in range(num_day):
    print(num_popul)
    num_popul = (num_popul + (num_popul * num_sum / 100))

