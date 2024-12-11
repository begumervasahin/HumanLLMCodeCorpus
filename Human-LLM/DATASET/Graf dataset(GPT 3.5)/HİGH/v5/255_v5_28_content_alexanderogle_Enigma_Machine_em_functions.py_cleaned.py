def fonk1(b9):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    b2 = b1.index(b9)
    b3 = b1[b2:] + b1[:b2]
    return b3, b2
def fonk2(b8, b3):
    b4 = []
    for char in b8:
        if char.isalpha():
            b4.append(b3[ord(char.lower()) - ord('a')])
        else:
            b4.append(char)
    return ''.join(b4)
def fonk3(b4, b3):
    b5 = []
    for char in b4:
        if char.isalpha():
            b5.append(chr(b3.index(char) + ord('a')))
        else:
            b5.append(char)
    return ''.join(b5)
def fonk4(b4):
    print("Encoded b8:")
    for char in b4:
        print(char, b6 = ' ')
def fonk5(size):
    return [0] * size
def fonk6(char):
    if len(char) != 1:
        print("Please input a single letter!")
    elif not char.isalpha():
        print("Please input a letter!")
    else:
        return ord(char.lower()) - ord('a')
if b7 = = "__main__":
    b8 = "Hello, World!"
    b9 = 'c'
    b3, b2 = fonk1(b9)
    b4 = fonk2(b8.lower(), b3)
    print("Encoded b8:", b4)
    b5 = fonk3(b4, b3)
    print("Decoded b8:", b5)