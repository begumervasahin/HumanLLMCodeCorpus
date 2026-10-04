def fonk1(text, shift_letter):
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b2 = b1.index(shift_letter)
    b3 = b1[b2:] + b1[:b2]
    b4 = [
        b3[b1.index(char)] if char.isalpha() else char
        for char in text
    ]
    b5 = ''.join(b4)
    print("\nOriginal Text:", text)
    print("\nShift Index:", b2)
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b5
def fonk2(text, shift_letter):
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b2 = b1.index(shift_letter)
    b3 = b1[b2:] + b1[:b2]
    b6 = [
        b1[b3.index(char)] if char.isalpha() else char
        for char in text
    ]
    b7 = ''.join(b6)
    print("\nEncoded Text:", text)
    print("\nShift Index:", b2)
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b7
def fonk3(text):
    print(' '.join(text))
def fonk4(size):
    return [0] * size
def fonk5(letter):
    if len(letter) != 1 or not letter.isalpha():
        print("That's not a letter!")
    else:
        b1 = list("abcdefghijklmnopqrstuvwxyz")
        return b1.index(letter)