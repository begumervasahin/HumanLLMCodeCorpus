def fonk1(hex_string):
    b1 = len(hex_string)
    b2 = [0] * b1
    for i in range(b1):
        b3 = fonk3(hex_string[2 * i])
        b4 = fonk3(hex_string[2 * i + 1])
        b2[i] = 16 * b3 + b4
    return b2
def fonk2(b2):
    return [hex(n)[2:].upper().zfill(2) for n in b2]
def fonk3(hex_digit):
    if hex_digit.isdigit():
        return int(hex_digit)
    return ord(hex_digit.upper()) - 55
def fonk4(byte_values):
    return [chr(b) for b in byte_values]
def fonk5(chars):
    a1 = 0
    for char in chars:
        a1 ^= ord(char)
    return chr(a1)
b5 = "48656C6C6F"
b2 = fonk1(b5)
b6 = fonk2(b2)
b7 = fonk4(b2)
a1 = fonk5(b7)
print(f"Hex Message: {b5}")
print(f"Decimal Values: {b2}")
print(f"Hex Values: {b6}")
print(f"Character Values: {b7}")
print(f"XOR Result: {a1}")