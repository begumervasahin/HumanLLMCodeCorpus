import random
def fonk1(size):
    b1 = []
    for _ in range(size):
        b1.append(random.randint(-size, size))
    return b1
def fonk2():
    b2 = []
    b3 = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    for size in b3:
        b2.append(fonk1(size))
    return b2