def fonk1(b10):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    b2 = b1.index(b10)
    b3 = b1[b2:] + b1[:b2]
    return b3, b2
def fonk2(b9, b3):
    b4 = []
    for char in b9:
        if char.isalpha():
            b5 = b3[ord(char.lower()) - ord('a')]
            b4.append(b5)
        else:
            b4.append(char)
    return ''.join(b4)
def fonk3(b4, b3):
    b6 = []
    for char in b4:
        if char.isalpha():
            b7 = chr(b3.index(char) + ord('a'))
            b6.append(b7)
        else:
            b6.append(char)
    return ''.join(b6)
def fonk4(b4):
    print(' '.join(b4))
if b8 = = "__main__":
    b9 = "Hello, World!"
    b10 = 'c'
    b3, b2 = fonk1(b10)
    b4 = fonk2(b9.lower(), b3)
    print("Encoded b9:", b4)
    print("Key Index:", b2)
    print("Substitution Alphabet:", b3)
    b6 = fonk3(b4, b3)
    print("\nDecoded b9:", b6)
    print("Key Index:", b2)
    print("Substitution Alphabet:", b3)