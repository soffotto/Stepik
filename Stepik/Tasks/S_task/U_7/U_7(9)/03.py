num = 56689932106
last = num % 10
count_3 = 0
count_last = 0
count_chet = 0
sum_5 = 0
count_7 = 0
pr_7 = 1
count_05 = 0

while num != 0:
    n = num % 10
    num //= 10
    if n == 3:
        count_3 += 1
    if n == last:
        count_last += 1
    if n % 2 == 0:
        count_chet += 1
    if n > 5:
        sum_5 += n
    if n > 7:
        count_7 += 1
        pr_7 *= n
        if count_7 == 1:
            pr_7 = n
        if count_7 == 0:
            pr_7 = 0
    if n == 5 or n== 0:
        count_05 += 1




print(count_3)
print(count_last)
print(count_chet)
print(sum_5)
print(pr_7)
print(count_05)