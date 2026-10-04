from random import randint
def power(x, y, p):
    return (x ** y) % p
def two_com(m, mlen):
    if m < 0:
        m = TwoComp(("{0:0%db}" % mlen).format(m))
    else:
        m = ("{0:0%db}" % mlen).format(m)
    return m
def decimal_to_binary(decimalin):
    binary_str = bin(int(decimalin))[2:]
    return binary_str
def adjust_size(key, size):
    if len(key) < size:
        return key.rjust(size, '0')
    elif len(key) > size:
        return key[:size]
    return key
def binary_to_decimal(binaryin):
    return int(binaryin, 2)
def random_binary(length):
    binary_str = ''.join(adjust_size(bin(randint(0, 255))[2:], 8) for _ in range(length
    binary_str = adjust_size(binary_str, length)
    return binary_to_decimal(binary_str)
def multiplicative_inverse(a, b):
    x, lx = 0, 1
    y, ly = 1, 0
    original_b = b
    while b != 0:
        q = a
        a, b = b, a % b
        lx, x = x, lx - q * x
        ly, y = y, ly - q * y
    if lx < 0:
        lx += original_b
    return lx