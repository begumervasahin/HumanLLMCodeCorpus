def fonk1(b4, a1):
    b1 = ""
    for char in b4:
        if char.isupper():
            b2 = chr((ord(char) + a1 - ord('A')) % 26 + ord('A'))
        else:
            b2 = chr((ord(char) + a1 - ord('a')) % 26 + ord('a'))
        b1 += b2
    return b1
if b3 = = "__main__":
    b4 = "Vineet"
    a1 = 4
    b1 = fonk1(b4, a1)
    print("ENCRYPTED TEXT:", b1)