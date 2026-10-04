def fonk1(msg):
    b1 = int(len(msg) / 2)
    b2 = [0] * b1
    for i in range(b1):
        b3 = fonk3(msg[2 * i])
        b4 = fonk3(msg[2 * i + 1])
        b2[i] = 16 * b3 + b4
    return b2
def fonk2(b8):
    return [hex(n).upper()[2:] for n in b8]
def fonk3(hex_val):
    if ord(hex_val) < 65:
        b5 = int(hex_val)
    else:
        b5 = ord(hex_val.upper()) - 55
    return b5
def fonk4(b2):
    return [chr(b) for b in b2]
def fonk5(chrs):
    b5 = 0
    for c in chrs:
        b5 ^= ord(c)
    return chr(b5)
if b6 = = "__main__":
    b7 = "4A6F686E20446F65"
    b8 = fonk1(b7)
    print(f"Hex to Nums: {b8}")
    b9 = fonk2(b8)
    print(f"Nums to Hex: {b9}")
    b10 = fonk4(b8)
    print(f"Bytes to Chars: {b10}")
    b11 = fonk5(b10)
    print(f"XOR of Chars: {b11}")