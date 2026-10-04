def fonk1(msg):
    b1 = len(msg)
    b2 = [0] * b1
    for i in range(b1):
        b3 = fonk3(msg[2 * i])
        b4 = fonk3(msg[2 * i + 1])
        b2[i] = 16 * b3 + b4
    return b2
def fonk2(b7):
    return [format(n, '02X') for n in b7]
def fonk3(hex_val):
    if hex_val.isdigit():
        return int(hex_val)
    return ord(hex_val.upper()) - ord('A') + 10
def fonk4(b2):
    return [chr(b) for b in b2]
def fonk5(chrs):
    a1 = 0
    for c in chrs:
        a1 ^= ord(c)
    return chr(a1)
if b5 = = "__main__":
    b6 = "4A6F686E20446F65"
    b7 = fonk1(b6)
    print(f"Hex to Nums: {b7}")
    b8 = fonk2(b7)
    print(f"Nums to Hex: {b8}")
    b9 = fonk4(b7)
    print(f"Bytes to Chars: {b9}")
    b10 = fonk5(b9)
    print(f"XOR of Chars: {b10}")