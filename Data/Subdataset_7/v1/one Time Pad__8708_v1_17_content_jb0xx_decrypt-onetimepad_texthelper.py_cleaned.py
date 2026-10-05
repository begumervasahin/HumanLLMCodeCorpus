def fonk1(msg):
    b1 = int(len(msg) / 2)
    b2 = [0] * b1
    for i in range(b1):
        b3 = fonk3(msg[2 * i])
        b4 = fonk3(msg[2 * i + 1])
        b2[i] = 16 * b3 + b4
    return b2
def fonk2(b7):
    return [hex(n).upper()[2:].zfill(2) for n in b7]
def fonk3(hexVal):
    if ord(hexVal) < 65:
        b5 = int(hexVal)
    else:
        b5 = ord(hexVal.upper()) - 55
    return b5
def fonk4(bytesArray):
    return [chr(b) for b in bytesArray]
def fonk5(chrs):
    b5 = 0
    for c in chrs:
        b5 ^= ord(c)
    return chr(b5)
b6 = "48656C6C6F20576F726C64"
b7 = fonk1(b6)
print("Numbers:", b7)
b8 = fonk2(b7)
print("Hexadecimal representation:", b8)
b9 = fonk4(b7)
print("Characters:", b9)
b10 = fonk5(b9)
print("XOR result:", b10)