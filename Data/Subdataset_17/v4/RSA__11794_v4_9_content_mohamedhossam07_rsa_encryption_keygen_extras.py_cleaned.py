from random import randint
def power(x, y, p):
    return (x ** y) % p
def two_com(m, mlen):
    if m < 0:
        m = TwoComp(("{0:0%db}" % mlen).format(m))
    else:
        m = ("{0:0%db}" % mlen).format(m)
    return m
def decimal(decimalin):
    decimalin = int(decimalin)
    binary_str = ""
    while True:
        binary_str += str(decimalin % 2)
        decimalin = decimalin
        if decimalin == 0:
            break
    return binary_str[::-1]
def size_be_R(key, size):
    if len(key) < size:
        x_key = key.rjust(size, '0')
    elif len(key) > size:
        x_key = key[:size]
    else:
        x_key = key
    return x_key
def binary2dec(binaryin):
    binaryin = str(binaryin)
    binaryintra = binaryin[::-1]
    binarydecimal = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(binaryintra))
    return binarydecimal
def rand_bin(leng):
    out = ''.join(size_be_R(bin(randint(0, 255))[2:], 8) for _ in range(int(leng / 8)))
    out = size_be_R(out, leng)
    return binary2dec(out)
def multiplicative_inverse(a, b):
    x, lx = 0, 1
    y, ly = 1, 0
    ob = b
    while b != 0:
        q = a
        a, b = b, a % b
        lx, x = x, lx - q * x
        ly, y = y, ly - q * y
    if lx < 0:
        lx += ob
    return lx