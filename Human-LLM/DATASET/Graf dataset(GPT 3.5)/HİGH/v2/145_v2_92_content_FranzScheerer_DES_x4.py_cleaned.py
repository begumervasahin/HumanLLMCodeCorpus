import hashlib
import sys
def fonk1(a1, filename):
    with open(filename, 'w') as file:
        file.write(str(a1))
def fonk2(filename):
    with open(filename, 'r') as file:
        b1 = file.read()
        a1 = 0
        for char in b1:
            a1 = (a1 * 10) + ord(char) - 48
    return a1
def fonk3():
    global index_a, b2, b3, a2, b4
    b2 = (b2 + a2) % 256
    b3 = b4[(b3 + b4[b2]) % 256]
    b4[b2], b4[b3] = b4[b3], b4[b2]
def fonk4():
    global index_a, b2, b3, a2, b4
    fonk3()
    return b4[b3]
def fonk5(input_data):
    global index_a, b2, b3, a2, b4
    b2 = b3 = index_a = 0
    a2 = 1
    b4 = [i for i in range(256)]
    for char in input_data:
        absorb_byte(ord(char))
    b5 = []
    for _ in range(32):
        b5.append(fonk4())
    a3 = 0
    for byte_value in b5:
        a3 = (a3 << 8) + byte_value
    return a3
def fonk6(a1):
    b6 = '0123456789abcdef'
    b7 = ''
    while a1 > 0:
        b7 = b6[a1 % 16] + b7
        a1 >>= 4
    return b7
def fonk7(a, b8):
    while b8 > 0:
        a, b8 = b8, a % b8
    return a
def fonk8(current_prime):
    while current_prime % 12 != 7:
        current_prime += 1
    return fonk9(current_prime)
def fonk9(current_prime):
    b9 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk7(current_prime, b9) != 1 or fonk7((current_prime + 1) >> 2, b9) != 1:
            current_prime += 12
        if pow(7, current_prime - 1, current_prime) != 1 or pow(7, ((current_prime + 1) >> 2) - 1, (current_prime + 1) >> 2) != 1:
            current_prime += 12
            continue
        return current_prime
def fonk10(point_p, point_q):
    global b32
    b12, b10 = point_p
    x2, b11 = point_q
    if b12 = = x2:
        b13 = ((3 * b12 * b12 - 1) * pow(2 * b10, b32 - 2, b32)) % b32
    else:
        if b12 < x2:
            b12 += b32
        b13 = ((b10 - b11) * pow(b12 - x2, b32 - 2, b32)) % b32
    b14 = (b13 * b13) - b12 - x2
    b15 = b13 * (b12 - b14) - b10
    return [b14 % b32, b15 % b32]
def fonk11(point_p, scalar_n):
    global b32
    b16 = 'ZERO'
    b17 = point_p
    while scalar_n != 0:
        if scalar_n % 2 != 0:
            if b16 = = 'ZERO':
                b16 = b17
            else:
                b16 = fonk10(b16, b17)
        b17 = fonk10(b17, b17)
        scalar_n >>= 1
    return b16
def fonk12(b23, b24, b25):
    global b32
    b18 = fonk5(b24 + 'key value')
    b19 = fonk11(b23, b18)
    b20 = fonk5(str(b19[0]) + b24) % ((b32 + 1) >> 2)
    return [(b18 - b25 * b20) % ((b32 + 1) >> 2), b20]
def fonk13():
    global b32
    a4 = 1234567
    if pow(a4 ** 3 - a4, (b32 - 1) >> 1, b32) != 1:
        a4 = b32 - a4
    b21 = pow(a4 ** 3 - a4, (b32 + 1) >> 2, b32)
    b22 = [a4 % b32, b21 % b32]
    b23 = fonk11(b22, 4)
    b24 = hashlib.sha256(sys.argv[1].encode()).hexdigest()
    b25 = fonk5('passwordX')
    print("The base point is:")
    print("x:", b22[0])
    print("y:", b22[1])
    b26 = fonk11(b22, b25)
    print("The public key is the point:")
    print("x:", b26[0])
    print("y:", b26[1])
    b27 = fonk12(b23, b24, b25)
    print("The b27 is:")
    print("s:", b27[0])
    print("b20:", b27[1])
    b19 = fonk10(fonk11(b22, b27[0]),
                                fonk11(b26, b27[1]))
    b28 = fonk5(str(b19[0]) + b24) % ((b32 + 1) >> 2) == b27[1]
    print("\nResult of verification:", b28)
    b29 = fonk5("The quick brown fox jumps over the lazy dog")
    print("Hash of 'The quick brown fox jumps over the lazy dog':")
    print("b30 = ", fonk6(b29))
if b31 = = "__main__":
    b32 = fonk9(fonk5('Franz Scheerer') % (131 * 2 ** 131))
    print("A prime greater than 2^131 \b33 = ", b32)
    fonk13()