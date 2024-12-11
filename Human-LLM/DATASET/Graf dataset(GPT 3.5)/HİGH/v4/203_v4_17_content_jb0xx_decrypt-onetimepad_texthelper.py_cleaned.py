def fonk1(msg):
    b1 = int(len(msg) / 2)
    b2 = [0] * b1
    for i in range(b1):
        b3 = fonk3(msg[2 * i])
        b4 = fonk3(msg[2 * i + 1])
        b2[i] = 16 * b3 + b4
    return b2
def fonk2(nums):
    return [hex(n).upper()[2:].zfill(2) for n in nums]
def fonk3(hex_val):
    if ord(hex_val) < 65:
        b5 = int(hex_val)
    else:
        b5 = ord(hex_val.upper()) - 55
    return b5
def fonk4(b2):
    return [chr(b) for b in b2]
def fonk5(chars):
    b5 = 0
    for c in chars:
        b5 ^= ord(c)
    return chr(b5)