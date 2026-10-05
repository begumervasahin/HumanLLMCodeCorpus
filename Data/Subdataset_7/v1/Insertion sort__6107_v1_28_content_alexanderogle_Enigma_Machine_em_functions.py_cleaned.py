def fonk1(string, n):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    b2 = b1.index(n)
    b3 = b1[b2:] + b1[:b2]
    b4 = []
    for char in string:
        if char.isalpha():
            b4.append(b3[b1.index(char)])
        else:
            b4.append(char)
    return ''.join(b4), b2, b3
def fonk2(string, n):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    b2 = b1.index(n)
    b3 = b1[b2:] + b1[:b2]
    b5 = []
    for char in string:
        if char.isalpha():
            b5.append(b1[b3.index(char)])
        else:
            b5.append(char)
    return ''.join(b5), b2, b3
def fonk3(string):
    print(' '.join(string))
def fonk4(size):
    return [0] * size
def fonk5(char):
    if len(char) != 1:
        print("That's not a single letter!")
        return None
    elif not char.isalpha():
        print("That's not a letter!")
        return None
    else:
        return ord(char.lower()) - ord('a')
if b6 = = "__main__":
    b7 = "Hello, World!"
    b8 = 'c'
    encoded, b2, b9 = fonk1(b7.lower(), b8)
    print("Encoded b7:", encoded)
    print("Key Index:", b2)
    print("Substitution Alphabet:", b9)
    decoded, b2, b9 = fonk2(encoded, b8)
    print("\nDecoded b7:", decoded)
    print("Key Index:", b2)
    print("Substitution Alphabet:", b9)