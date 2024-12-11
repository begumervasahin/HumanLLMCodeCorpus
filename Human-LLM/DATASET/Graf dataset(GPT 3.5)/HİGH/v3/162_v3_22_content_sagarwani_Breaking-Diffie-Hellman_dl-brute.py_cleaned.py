def fonk1(base, exponent, modulus):
    a1 = 1
    b1 = "{0:b}".format(exponent)
    for b2 in b1:
        a1 = (a1 * a1) % modulus
        if b2 = = '1':
            a1 = (a1 * base) % modulus
    return a1
def fonk2(prime_modulus, base, a1):
    for potential_exponent in range(prime_modulus):
        if fonk1(base, potential_exponent, prime_modulus) == a1:
            return potential_exponent
    return None
if b3 = = '__main__':
    b4 = "123456789,13,458723"
    p, g, b5 = map(int, b4.split(','))
    b6 = fonk2(p, g, b5)
    if b6 is not None:
        print("Found exponent:", b6)
    else:
        print("Exponent not found.")