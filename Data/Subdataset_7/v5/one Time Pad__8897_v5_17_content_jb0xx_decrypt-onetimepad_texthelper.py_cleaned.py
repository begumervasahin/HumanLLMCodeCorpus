def fonk1(hex_msg):
    b1 = len(hex_msg)
    b2 = []
    for i in range(b1):
        b3 = fonk3(hex_msg[2 * i])
        b4 = fonk3(hex_msg[2 * i + 1])
        b2.append(16 * b3 + b4)
    return b2
def fonk2(b2):
    return [hex(n)[2:].upper().zfill(2) for n in b2]
def fonk3(hex_digit):
    if ord(hex_digit) < 65:
        return int(hex_digit)
    else:
        return ord(hex_digit.upper()) - 55
def fonk4(byte_list):
    return [chr(b) for b in byte_list]
def fonk5(char_list):
    a1 = 0
    for char in char_list:
        a1 ^= ord(char)
    return chr(a1)