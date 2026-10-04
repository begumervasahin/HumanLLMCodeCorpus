def fonk1(filename_path):
    b1 = ''
    with open(filename_path, b2 = 'rb') as file:
        b3 = file.read()
    for i in range(len(b3)):
        b4 = b3[i]
        b5 = bin(b4)
        if (len(b5) > 8):
            b5 = b5[2:]
        b6 = 8 - len(b5)
        for j in range(b6):
            b1 += '0'
        b1 += b5
    return b1.replace('b', '0')
def fonk2(binary):
    b7 = bytearray()
    for i in range(0, len(binary), 8):
        b8 = binary[i:i+8]
        b7.append(int(b8,2))
    return b7
def fonk3(hex_key):
    b9 = []
    b10 = ""
    for char in hex_key:
        b11 = "{:04b}".format(int(char, 16))
        b10 += b11
    return b10