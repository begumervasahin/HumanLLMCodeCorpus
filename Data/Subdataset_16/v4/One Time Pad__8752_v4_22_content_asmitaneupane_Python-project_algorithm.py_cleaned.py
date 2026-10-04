def fonk1(b3, b4):
    b1 = []
    b2 = len(b3)
    for i, char in enumerate(b4):
        b1.append(chr(ord(char) ^ ord(b3[i % b2])))
    return ''.join(b1)
b3 = "mysecretkey"
b4 = "Hello, World!"
b5 = fonk1(b3, b4)
print("Cipher Text:", b5)
b6 = fonk1(b3, b5)
print("Decrypted Text:", b6)