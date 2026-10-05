def fonk1(b16):
    b1 = [...]
    b2 = [...]
    b3 = [()]*44
    for i in range(b6):
        b3[i] = (b16[b6*i], b16[b6*i+1], b16[b6*i+2], b16[b6*i+3])
    for i in range(b6, 44):
        b4 = b3[i-1]
        b5 = b3[i-b6]
        if i % b6 = = 0:
            b4 = fonk4(b4)
            b4 = fonk5(b4)
            b4 = fonk6(b4, b2[int(i/b6)])
        b5 = ''.join(b5)
        b4 = ''.join(b4)
        b7 = fonk2(b5, b4)
        b3[i] = (b7[:2], b7[2:b6], b7[b6:6], b7[6:8])
    return b3
def fonk2(hex1, hex2):
    b8 = fonk3(hex1)
    b9 = fonk3(hex2)
    b7 = int(b8, 2) ^ int(b9, 2)
    b10 = hex(b7)[2:].zfill(8)
    return b10
def fonk3(hex):
    return bin(int(hex, 16))
def fonk4(b5):
    return b5[1:] + b5[:1]
def fonk5(b5):
    b11 = ()
    for i in range(b6):
        b15, b12 = fonk7(b5[i])
        b13 = (b15 * 16) + b12
        b14 = format(b1[b13], '02x')
        b11 += (b14,)
    return b11
def fonk6(b5, rcon_value):
    return fonk2(b5, format(rcon_value, '02x'))
def fonk7(hex_val):
    if hex_val[0].isdigit():
        b15 = int(hex_val[0]) + 1
    else:
        b15 = ord(hex_val[0]) - ord('a') + 10
    if hex_val[1].isdigit():
        b12 = int(hex_val[1]) + 1
    else:
        b12 = ord(hex_val[1]) - ord('a') + 10
    return b15, b12
def fonk8(b17):
    print("\n\nKey Schedule: \n")
    for i, b5 in enumerate(b17):
        print(f"b3{i} = {' '.join(b5)}")
def fonk9():
    b16 = ["0f", "15", "71", "c9", "47", "d9", "e8", "59", "0c", "b7", "ad", "d6", "af", "7f", "67", "98"]
    b17 = fonk1(b16)
    print("Original Key: " + "".join(b16))
    fonk8(b17)
if b18 = = '__main__':
    fonk9()