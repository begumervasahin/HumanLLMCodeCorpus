def fonk1(b5, b6):
    b1 = []
    for i, char in enumerate(b5):
        b2 = b6[i % len(b6)]
        if char.isupper():
            b3 = chr((ord(char) + ord(b2) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            b3 = chr((ord(char) + ord(b2) - ord('a') - ord('A')) % 26 + ord('a'))
        else:
            b3 = char
        b1.append(b3)
    return ''.join(b1)
if b4 = = "__main__":
    b5 = "VINeeT"
    b6 = "WOW"
    b7 = fonk1(b5, b6)
    print("ENCRYPTED TEXT:", b7)