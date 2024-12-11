import sys
import hashlib
b1 = b3 = b7 = a1 = 0
b2 = []
def fonk1(input_string):
    global b1, b3, b7, a1, b2
    b3 = b7 = b1 = 0
    a1 = 1
    b2 = [ix for ix in range(256)]
    for c in input_string:
        absorb_byte241(ord(c))
    b4 = []
    squeeze241(b4, 32)
    a2 = 0
    for bx in b4:
        a2 = (a2 << 8) + bx
    return a2
def fonk2(number):
    b5 = '0123456789abcdef'
    b6 = ''
    while number > 0:
        b6 = b5[number % 16] + b6
        number >>= 4
    return b6
def fonk3():
    global b1, b3, b7, a1, b2
    b3 = (b3 + a1) % 256
    b7 = b2[(b7 + b2[b3]) % 256]
    b2[b3], b2[b7] = b2[b7], b2[b3]
def fonk4():
    global b1, b3, b7, a1, b2
    fonk3()
    return b2[b7]
def fonk5():
    global b1, b3, b7, a1, b2
    for _ in range(256):
        fonk3()
    a1 = (a1 + 2) % 256
    b1 = 0
def fonk6(byte_value):
    global b1, b3, b7, a1, b2
    if b1 = = 241:
        fonk5()
    b2[b1], b2[240 + byte_value] = b2[240 + byte_value], b2[b1]
    b1 += 1
def fonk7(byte_value):
    fonk6(byte_value % 16)
    fonk6(byte_value >> 4)
def fonk8(output_list, output_length):
    global b1, b3, b7, a1, b2
    fonk5()
    for _ in range(output_length):
        output_list.append(fonk4())
def fonk9(point1, point2, b31):
    b10, b8 = point1[0], point2[0]
    y1, b9 = point1[1], point2[1]
    if b10 = = b8:
        b11 = ((3 * b10 * b10 - 1) * pow(2 * y1, b31 - 2, b31)) % b31
    else:
        if b10 < b8:
            b10 += b31
        b11 = ((y1 - b9) * pow(b10 - b8, b31 - 2, b31)) % b31
    b12 = (b11 * b11) - b10 - b8
    b13 = b11 * (b10 - b12) - y1
    return [b12 % b31, b13 % b31]
def fonk10(point, scalar, b31):
    b14 = 'ZERO'
    b15 = point
    while scalar != 0:
        if scalar % 2 != 0:
            if b14 = = 'ZERO':
                b14 = b15
            else:
                b14 = fonk9(b14, b15, b31)
        b15 = fonk9(b15, b15, b31)
        scalar >>= 1
    return b14
def fonk11(b23, b24, b25, b31):
    b16 = fonk1(b24 + 'key value')
    b17 = fonk10(b23, b16, b31)
    b18 = fonk1(str(b17[0]) + b24) % ((b31 + 1) >> 2)
    return [(b16 - b25 * b18) % ((b31 + 1) >> 2), b18]
def fonk12(current_prime):
    b19 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk13(current_prime, b19) != 1 or fonk13((current_prime + 1) >> 2, b19) != 1:
            current_prime += 12
        if pow(7, current_prime - 1, current_prime) != 1 or pow(7, ((current_prime + 1) >> 2) - 1, (current_prime + 1) >> 2) != 1:
            current_prime += 12
            continue
        return current_prime
def fonk13(a, b20):
    while b20 > 0:
        a, b20 = b20, a % b20
    return a
def fonk14():
    global b31
    a3 = 1234567
    if pow(a3 ** 3 - a3, (b31 - 1) >> 1, b31) != 1:
        a3 = b31 - a3
    b21 = pow(a3 ** 3 - a3, (b31 + 1) >> 2, b31)
    b22 = [a3 % b31, b21 % b31]
    b23 = fonk10(b22, 4, b31)
    b24 = hashlib.sha256(sys.argv[1].encode()).hexdigest()
    b25 = fonk1('passwordX')
    print("The base point is:")
    print("x:", b22[0])
    print("y:", b22[1])
    b26 = fonk10(b22, b25, b31)
    print("The public key is the point:")
    print("x:", b26[0])
    print("y:", b26[1])
    b27 = fonk11(b23, b24, b25, b31)
    print("The b27 is:")
    print("s:", b27[0])
    print("b18:", b27[1])
    b17 = fonk9(fonk10(b22, b27[0], b31),
                   fonk10(b26, b27[1], b31))
    b28 = fonk1(str(b17[0]) + b24) % ((b31 + 1) >> 2) == b27[1]
    print("\nResult of verification:", b28)
    b29 = fonk1("The quick brown fox jumps over the lazy dog")
    print("Hash of 'The quick brown fox jumps over the lazy dog' is:", fonk2(b29))
if b30 = = "__main__":
    b31 = fonk12(fonk1('Franz Scheerer') % (131 * 2 ** 131))
    print("A prime greater than 2^131 \b32 = ", b31)
    fonk14()