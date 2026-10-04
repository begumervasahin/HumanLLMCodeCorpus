def fonk1(b6, b7):
    b1 = []
    b2 = len(b7)
    for i, char in enumerate(b6):
        b3 = b7[i % b2]
        if char.isupper():
            b4 = chr((ord(char) + ord(b3) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            b4 = chr((ord(char) + ord(b3) - ord('a') - ord('A')) % 26 + ord('a'))
        else:
            b4 = char
        b1.append(b4)
    return ''.join(b1)
if b5 = = "__main__":
    b6 = "VINeeT"
    b7 = "WOW"
    b1 = fonk1(b6, b7)
    print("ENCRYPTED TEXT:", b1)