def fonk1(b3: str, b4: str) -> str:
    b1 = []
    b2 = len(b3)
    for i, char in enumerate(b4):
        b1.append(chr(ord(char) ^ ord(b3[i % b2])))
    return ''.join(b1)
def fonk2() -> None:
    b3 = "SECRET"
    b4 = "HELLO WORLD"
    b5 = fonk1(b3, b4)
    print("Encrypted:", b5)
    b6 = fonk1(b3, b5)
    print("Decrypted:", b6)
if b7 = = "__main__":
    fonk2()