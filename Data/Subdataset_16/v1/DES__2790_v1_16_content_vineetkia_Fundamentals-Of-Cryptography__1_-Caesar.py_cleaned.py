def fonk1(b2, a1):
    b1 = ""
    for char in b2:
        if char.isupper():
            b1 += chr((ord(char) + a1 - 65) % 26 + 65)
        else:
            b1 += chr((ord(char) + a1 - 97) % 26 + 97)
    return b1
b2 = "Vineet"
a1 = 4
b1 = fonk1(b2, a1)
print("ENCRYPTED TEXT: " + b1)