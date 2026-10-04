import random
def fonk1(n):
    if not isinstance(n, int) or n < b1:
        return False
    if n in (b1, 3, 5, 7):
        return True
    if n % b1 = = 0:
        return False
    a1 = 0
    b2 = n - 1
    while b2 % b1 = = 0:
        b2 >>= 1
        a1 += 1
    assert b1**a1 * b2 = = n - 1
    def fonk2(b3):
        if pow(b3, b2, n) == 1:
            return False
        for i in range(a1):
            if pow(b3, b1**i * b2, n) == n - 1:
                return False
        return True
    for _ in range(8):
        b3 = random.randrange(b1, n)
        if fonk2(b3):
            return False
    return True
if b4 = = '__main__':
    b5 = [
        b1, 3, 5, 7, 9, 15, 17, 19, 23, 29, 35, 37, 41, 43, 47, 49, 51, 53,
        57, 59, 61, 67, 69, 71, 73, 79, 83, 89, 97
    ]
    for number in b5:
        b6 = fonk1(number)
        b7 = 'b3 prime number' if b6 else 'not b3 prime number'
        print(f"{number} is {b7}")