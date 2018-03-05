# INPUT values
l = str(input())


def keyboard(letter):
    keyboard = "qwertyuiopasdfghjklzxcvbnm"
    if letter == 'm':
        return 'q'
    return keyboard[keyboard.index(letter) + 1]
print(keyboard(l))
