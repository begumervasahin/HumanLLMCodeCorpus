def fonk1(b5, b6):
    b1 = ""
    for i in range(len(b5)):
        b2 = i % len(b6)
        if b5[i].isupper():
            b3 = chr((ord(b5[i]) + ord(b6[b2]) - 2 * ord('A')) % 26 + ord('A'))
        elif b5[i].islower():
            b3 = chr((ord(b5[i]) + ord(b6[b2]) - ord('a') - ord('A')) % 26 + ord('a'))
        else:
            b3 = b5[i]
        b1 += b3
    return b1
if b4 = = "__main__":
    b5 = "VINeeT"
    b6 = "WOW"
    b7 = fonk1(b5, b6)
    print("ENCRYPTED TEXT:", b7)