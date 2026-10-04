def fonk1(b5):
    b1 = ''
    with open(b5, 'rb') as file:
        b2 = file.read()
    for byte in b2:
        b1 += bin(byte)[2:].zfill(8)
    return b1
def fonk2(binary_str):
    b3 = bytearray(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
    return b3
def fonk3(b7):
    b4 = ''.join(f'{int(char, 16):04b}' for char in b7)
    return b4
def fonk4():
    b5 = 'example.bin'
    b6 = fonk1(b5)
    print("Binary content of file:", b6)
    b3 = fonk2(b6)
    print("Bytearray:", b3)
    b7 = '1a2b3c'
    b4 = fonk3(b7)
    print("Binary key:", b4)
if b8 = = "__main__":
    fonk4()