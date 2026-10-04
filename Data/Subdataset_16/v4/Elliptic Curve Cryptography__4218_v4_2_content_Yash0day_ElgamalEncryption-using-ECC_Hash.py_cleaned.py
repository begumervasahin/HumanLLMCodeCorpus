def fonk1(char):
    return ord(char) + 100
def fonk2(modified_ascii):
    return int(modified_ascii) - 100
def fonk3(message):
    b1 = ''.join(str(fonk1(char)).zfill(3) for char in message)
    return b1
def fonk4(b1):
    b2 = ''.join(
        chr(fonk2(b1[i:i+3]))
        for i in range(0, len(b1), 3)
    )
    return b2
if b3 = = "__main__":
    b4 = "Hello, World!"
    print("Original Message:", b4)
    b1 = fonk3(b4)
    print("Encoded Message:", b1)
    b2 = fonk4(b1)
    print("Decoded Message:", b2)