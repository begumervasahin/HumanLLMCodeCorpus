def fonk1(msg):
    b1 = len(msg)
    b2 = [0] * b1
    for i in range(b1):
        b3 = fonk3(msg[2 * i])
        b4 = fonk3(msg[2 * i + 1])
        b2[i] = 16 * b3 + b4
    return b2
def fonk2(nums):
    return [hex(n)[2:].upper().zfill(2) for n in nums]
def fonk3(hex_val):
    if hex_val.isdigit():
        return int(hex_val)
    return ord(hex_val.upper()) - 55
def fonk4(b2):
    return [chr(b) for b in b2]
def fonk5(chrs):
    a1 = 0
    for c in chrs:
        a1 ^= ord(c)
    return chr(a1)