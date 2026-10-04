import time
def fonk1(b1):
    if b1 < 2:
        return False
    if b1 = = 2:
        return True
    for b2 in range(2, int(b1 * 0.5 + 1)):
        if b1 % b2 = = 0:
            return False
    return True
def fonk2(limit):
    b3 = time.time()
    b4 = []
    for b2 in range(limit):
        if fonk1(b2):
            b4.append(b2)
    print(b4)
    for prime in b4:
        b5 = 2 ** prime - 1
        if fonk1(b5):
            b6 = time.time() - b3
            print(f"Time elapsed: {b6:.2f} seconds")
            b7 = 2 ** (prime - 1) * b5
            print(f"Mersenne prime: {b7}")
if b8 = = "__main__":
    fonk2(10000)