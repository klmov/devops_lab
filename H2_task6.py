# INPUT values
l = str(input())


def decode(string):
    res = ""

    def convert(num):
        n = int(num, 27)
        return n
    # According to task our alphabet starts from a:1 and 27 is space.
    alph = " abcdefghijklmnopqrstuvwxyz "
    for i in range(len(string)):
        for x in range(1, 27):
            if (x + i) % 27 == convert(string[i]):
                res += (alph[x - 1])
    return res
print(decode(l))
