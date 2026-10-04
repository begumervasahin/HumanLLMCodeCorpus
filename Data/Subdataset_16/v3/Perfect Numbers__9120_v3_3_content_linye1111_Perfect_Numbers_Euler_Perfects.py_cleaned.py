import time
def fonk1(b1):
    if b1 < 2:
        return False
    if b1 = = 2:
        return True
    for b2 in range(2, int(b1 ** 0.5) + 1):
        if b1 % b2 = = 0:
            return False
    return True
def fonk2(limit):
    b3 = [b2 for b2 in range(limit) if fonk1(b2)]
    return b3
def fonk3():
    b4 = time.time()
    b3 = fonk2(10000)
    print(b3)
    for prime in b3:
        b5 = 2 ** prime - 1
        if fonk1(b5):
            b6 = time.time() - b4
            print(f"Time elapsed: {b6} seconds")
            print(f"Mersenne prime: {2 ** (prime - 1) * b5}")
if b7 = = '__main__':
    fonk3()