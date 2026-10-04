def fonk1(b2, b3):
    b1 = [
        chr(ord(char) ^ ord(b2[i % len(b2)]))
        for i, char in enumerate(b3)
    ]
    return ''.join(b1)
def fonk2():
    b2 = "mysecretkey"
    b3 = "Hello, World!"
    b1 = fonk1(b2, b3)
    print("Cipher Text:", b1)
    b4 = fonk1(b2, b1)
    print("Decrypted Text:", b4)
if b5 = = "__main__":
    fonk2()