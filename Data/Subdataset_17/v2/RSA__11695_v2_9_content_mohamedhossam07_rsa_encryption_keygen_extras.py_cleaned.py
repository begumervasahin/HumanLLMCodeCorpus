from random import randint
def power(x, y, p):
    return (x ** y) % p
def two_com(m, mlen):
    if m < 0:
        m = TwoComp(f"{m:0{mlen}b}")
    else:
        m = f"{m:0{mlen}b}"
    return m
def decimal(decimalin):
    decimalin = int(decimalin)
    binary_rep = ""
    while decimalin > 0:
        binary_rep = str(decimalin % 2) + binary_rep
        decimalin
    return binary_rep or "0"
def size_be_R(key, size):
    if len(key) < size:
        return key.rjust(size, '0')
    elif len(key) > size:
        return key[:size]
    return key
def binary2dec(binaryin):
    binaryin = binaryin[::-1]
    decimal_value = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(binaryin))
    return decimal_value
def rand_bin(length):
    binary_str = ''.join(size_be_R(bin(randint(0, 10))[2:], 8) for _ in range(length
    binary_str = size_be_R(binary_str, length)
    return binary2dec(binary_str)
def multiplicative_inverse(a, b):
    x, y, lx, ly = 0, 1, 1, 0
    oa, ob = a, b
    while b != 0:
        q = a
        a, b = b, a % b
        x, lx = lx - q * x, x
        y, ly = ly - q * y, y
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx
print(power(2, 5, 13))
print(two_com(-5, 8))
print(decimal(13))
print(size_be_R('101', 8))
print(binary2dec('1101'))
print(rand_bin(16))
print(multiplicative_inverse(17, 3120))
