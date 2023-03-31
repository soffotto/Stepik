l_1 = [2, 45, 2, 3, 5, 67]
l_2 =[3, 4, 6, 22, 72]

def merge(l_1, l_2):
    # l_1.extend(l_2)
    # l_1.sort()
    # return l_1
    return sorted(l_1 + l_2)

# n_1 = [int(c) for c in input().split()]
# n_2 = [int(c) for c in input().split()]

print(merge(l_1, l_2))


