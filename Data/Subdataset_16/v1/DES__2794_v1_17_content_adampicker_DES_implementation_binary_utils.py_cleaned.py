def fonk1(b9):
    b1 = ''
    with open(b9, b2 = 'rb') as file:
        b3 = file.read()
    for b6 in b3:
        b4 = bin(b6)[2:].zfill(8)
        b1 += b4
    return b1
def fonk2(binary):
    b5 = bytearray()
    for i in range(0, len(binary), 8):
        b6 = binary[i:i+8]
        b5.append(int(b6, 2))
    return b5
def fonk3(b11):
    b7 = ''.join("{:04b}".format(int(char, 16)) for char in b11)
    return b7
if b8 = = "__main__":
    b9 = 'example.bin'
    b10 = fonk1(b9)
    print("Binary content of file:", b10)
    b5 = fonk2(b10)
    print("Bytearray:", b5)
    b11 = '1a2b3c'
    b7 = fonk3(b11)
    print("Binary key:", b7)