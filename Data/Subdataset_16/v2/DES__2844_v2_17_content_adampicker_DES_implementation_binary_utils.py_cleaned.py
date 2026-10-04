def fonk1(b6):
    b1 = ''
    with open(b6, 'rb') as file:
        b2 = file.read()
    for byte in b2:
        b1 += bin(byte)[2:].zfill(8)
    return b1
def fonk2(binary_str):
    b3 = bytearray()
    for i in range(0, len(binary_str), 8):
        b4 = binary_str[i:i+8]
        b3.append(int(b4, 2))
    return b3
def fonk3(b8):
    b5 = ''.join("{:04b}".format(int(char, 16)) for char in b8)
    return b5
def fonk4():
    b6 = 'example.bin'
    b7 = fonk1(b6)
    print("Binary content of file:", b7)
    b3 = fonk2(b7)
    print("Bytearray:", b3)
    b8 = '1a2b3c'
    b5 = fonk3(b8)
    print("Binary key:", b5)
if b9 = = "__main__":
    fonk4()