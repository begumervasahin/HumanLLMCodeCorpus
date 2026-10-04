def fonk1(char):
    return ord(char) + 100
def fonk2(modified_ascii):
    return int(modified_ascii) - 100
def fonk3(message):
    return ''.join(str(fonk1(char)).zfill(3) for char in message)
def fonk4(b3):
    return ''.join(chr(fonk2(b3[i:i+3])) for i in range(0, len(b3), 3))
if b1 = = "__main__":
    b2 = "Hello, World!"
    print("Original Message:", b2)
    b3 = fonk3(b2)
    print("Encoded Message:", b3)
    b4 = fonk4(b3)
    print("Decoded Message:", b4)