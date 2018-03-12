from collections import OrderedDict
# Creating ordered dictionary, which counts occurences
n = int(input())  # Number of words


def word_order(n):
    dict1 = OrderedDict()
    for i in range(n):
        words = input()  # Words
        if words not in dict1.keys():
            dict1.update({words: 1})
            continue
        dict1[words] += 1

    print(len(dict1.keys()))
    print(*dict1.values())
word_order(n)
