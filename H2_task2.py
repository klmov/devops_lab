n = int(input())  # Number of items in list
l = []
# Creating list
for i in range(n):
    l.append(int(input()))


def fun2(n, l):
    max_frq = 1
    for i in range(n):
        frq = 1
        for k in range(i+1, n):
            if l[i] == l[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = l[i]
    if max_frq > 1:
        return(num)

print(fun2(n, l))
