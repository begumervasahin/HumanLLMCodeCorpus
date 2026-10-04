def fonk1(text, shift_letter):
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b2 = b1.index(shift_letter)
    b3 = b1[b2:] + b1[:b2]
    b4 = []
    for char in text:
        if char.isalpha():
            b4.append(b3[b1.index(char)])
        else:
            b4.append(char)
    b5 = ''.join(b4)
    print("\nOriginal Text: ", text)
    print("\nShift b6 = ", b2)
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b5
def fonk2(text, shift_letter):
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b2 = b1.index(shift_letter)
    b3 = b1[b2:] + b1[:b2]
    b7 = []
    for char in text:
        if char.isalpha():
            b7.append(b1[b3.index(char)])
        else:
            b7.append(char)
    b8 = ''.join(b7)
    print("\nEncoded Text: ", text)
    print("\nShift b6 = ", b2)
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b8
def fonk3(text):
    print(' '.join(list(text)))
def fonk4(size):
    return [0] * size
def fonk5(letter):
    if len(letter) != 1 or not letter.isalpha():
        print("That's not a letter!")
    else:
        b1 = list("abcdefghijklmnopqrstuvwxyz")
        return b1.index(letter)