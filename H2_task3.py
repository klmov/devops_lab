# Input values
left = int(input())
right = int(input())


def selfDividingNumbers(left, right):
    def isDivNum(num):
        n = str(num)
        for i in str(num):
            if int(i) == 0 or num % int(i) != 0:
                return False
        return True
    res = []
    for num in range(left, right + 1):
        if isDivNum(num):
            res.append(num)
    return res
print(selfDividingNumbers(left, right))
