from collections import OrderedDict
# Creating ordered dictionary, which counts occurences
n = int(input())  # Number of words


def word_order(n):
    dict = OrderedDict()
    for i in range(n):
        words = input()  # Words
        if words not in dict.keys():
            dict.update({words: 1})
            continue
        dict[words] += 1

    print(len(dict.keys()))
    print(*dict.values())
word_order(n)
