num = int(input())
l = []
for i in range(num):
    l.append(input())
k = int(input())
s = ''
for i in l:
    if len(i) >= k:
        s += i[k-1]
print(s)
