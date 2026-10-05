def fonk1(hex_string):
    b1 = len(hex_string)
    b2 = []
    for i in range(b1):
        b3 = fonk3(hex_string[2 * i])
        b4 = fonk3(hex_string[2 * i + 1])
        b2.append(16 * b3 + b4)
    return b2
def fonk2(b2):
    return [format(n, '02X') for n in b2]
def fonk3(hex_val):
    if ord(hex_val) < 65:
        b5 = int(hex_val)
    else:
        b5 = ord(hex_val.upper()) - 55
    return b5
def fonk4(byte_list):
    return [chr(byte) for byte in byte_list]
def fonk5(char_list):
    a1 = 0
    for char in char_list:
        a1 ^= ord(char)
    return chr(a1)
b6 = "48656C6C6F20576F726C64"
b7 = fonk1(b6)
print("Decimal List:", b7)
b8 = fonk2(b7)
print("Hexadecimal Representation:", b8)
b9 = fonk4(b7)
print("Character List:", b9)
b10 = fonk5(b9)
print("XOR Result:", b10)