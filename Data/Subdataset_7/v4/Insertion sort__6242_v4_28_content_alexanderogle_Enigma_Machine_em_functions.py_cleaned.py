def fonk1(text, b11):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    print("Original b10:", text)
    b2 = b1.index(b11)
    b3 = b1[b2:] + b1[:b2]
    print("Key Index:", b2)
    print("Substitution Alphabet:", ' '.join(b3))
    b4 = []
    for char in text:
        if char.isalpha():
            b4.append(b3[b1.index(char)])
        else:
            b4.append(char)
    b5 = ''.join(b4)
    return b5
def fonk2(text, b11):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    print("Encoded b10:", text)
    b2 = b1.index(b11)
    b3 = b1[b2:] + b1[:b2]
    print("Key Index:", b2)
    print("Substitution Alphabet:", ' '.join(b3))
    b6 = []
    for char in text:
        if char.isalpha():
            b6.append(b1[b3.index(char)])
        else:
            b6.append(char)
    b7 = ''.join(b6)
    return b7
def fonk3(text):
    print("Encoded b10:")
    for char in text:
        print(char, b8 = ' ')
def fonk4(size):
    return [0] * size
def fonk5(char):
    if len(char) != 1:
        print("Please input a single letter!")
    elif not char.isalpha():
        print("Please input a letter!")
    else:
        return ord(char.lower()) - ord('a')
if b9 = = "__main__":
    b10 = "Hello, World!"
    b11 = 'c'
    b4 = fonk1(b10.lower(), b11)
    print("Encoded b10:", b4)
    b6 = fonk2(b4, b11)
    print("Decoded b10:", b6)