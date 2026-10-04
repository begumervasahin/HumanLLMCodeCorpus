import math
import time
def fonk1(number):
    if number % b1 = = 0:
        number -= 1
    else:
        number -= b1
    return number
def fonk2(b2, b):
    if b2 = = 0:
        return (b, 0, 1)
    else:
        g, b4, b3 = fonk2(b % b2, b2)
        return (g, b3 - (b
def fonk3(b2, m):
    g, b3, b4 = fonk2(b2, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return b3 % m
def fonk4(n, e):
    b5 = time.time()
    b6 = math.floor(math.sqrt(n))
    b6 = fonk1(b6)
    for b7 in range(b6, 1, -b1):
        if n % b7 = = 0:
            b8 = b7
            break
    b9 = n
    if n != b8 * b9:
        raise Exception('Factorization failed')
    b10 = (b8 - 1) * (b9 - 1)
    b11 = fonk3(e, b10)
    if b11 * e % b10 != 1:
        raise Exception('Modular inverse calculation failed')
    b12 = time.time() - b5
    return (b11, b12)
b13 = [
    (1325147, 79), (13339787, 351047), (87411743, 11), (153988391, 365),
    (642281891, 80105), (3662937263, 80273), (2461987247, 78703),
    (10988963221, 118297), (9979645019, 9764819), (36207914857, 89)
]
b12 = 0
for n, e in b13:
    b11, b14 = fonk4(n, e)
    print(f'Key pair (n, e): ({n}, {e})')
    print(f'Private key b11: {b11}')
    print(f'Time taken: {b14:.6f} seconds')
    b12 += b14
print(f'Total time: {b12:.6f} seconds')