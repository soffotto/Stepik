# def is_one_away(word1, word2):
#     return len(word1) == len(word2)
#
# w_1 = 'asdsfe'
# w_2 = 'dfghr'
#
# print( is_one_away(w_1, w_2))

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

w_1 = 'asdf'
w_2 = 'fasd'

print( is_one_away(w_1, w_2))