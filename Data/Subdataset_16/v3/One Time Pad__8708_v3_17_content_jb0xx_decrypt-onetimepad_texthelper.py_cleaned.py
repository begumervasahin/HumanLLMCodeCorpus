def fonk1(msg):
    b1 = len(msg)
    return [16 * fonk3(msg[2 * i]) + fonk3(msg[2 * i + 1]) for i in range(b1)]
def fonk2(b4):
    return [format(n, '02X') for n in b4]
def fonk3(hex_val):
    return int(hex_val, 16)
def fonk4(bytes_array):
    return [chr(b) for b in bytes_array]
def fonk5(chrs):
    a1 = 0
    for c in chrs:
        a1 ^= ord(c)
    return chr(a1)
if b2 = = "__main__":
    b3 = "4A6F686E20446F65"
    b4 = fonk1(b3)
    print(f"Hex to Nums: {b4}")
    b5 = fonk2(b4)
    print(f"Nums to Hex: {b5}")
    b6 = fonk4(b4)
    print(f"Bytes to Chars: {b6}")
    b7 = fonk5(b6)
    print(f"XOR of Chars: {b7}")