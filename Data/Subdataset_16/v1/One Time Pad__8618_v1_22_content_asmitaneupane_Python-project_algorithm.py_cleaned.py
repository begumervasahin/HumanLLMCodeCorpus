def fonk1(b2, b3):
    b1 = ""
    a1 = 0
    for char in b3:
        b1 += chr(ord(char) ^ ord(b2[a1]))
        a1 += 1
        if a1 = = len(b2):
            a1 = 0
    return b1
def fonk2():
    b2 = "SECRET"
    b3 = "HELLO WORLD"
    b4 = fonk1(b2, b3)
    print("Encrypted:", b4)
    b5 = fonk1(b2, b4)
    print("Decrypted:", b5)
if b6 = = "__main__":
    fonk2()