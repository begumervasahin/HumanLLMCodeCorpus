def fonk1(base, exponent, modulus):
    b1 = bin(exponent)[2:][::-1]
    b2 = len(b1)
    b3 = [base]
    b4 = base
    for _ in range(b2 - 1):
        b5 = (b4 * b4) % modulus
        b3.append(b5)
        b4 = b5
    b6 = fonk2(b3, b1, modulus)
    return b6 % modulus
def fonk2(array, b1, modulus):
    b6 = 1
    for index, base_power in enumerate(array):
        if int(b1[index]) == 0:
            continue
        b6 *= base_power
        b6 = b6 % modulus
    return b6
print(fonk1(2, 6, 10000000))