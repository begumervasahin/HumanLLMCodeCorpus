import random
def fonk1(size):
    return [random.randint(-size, size) for _ in range(size)]
def fonk2():
    b1 = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    b2 = [fonk1(size) for size in b1]
    return b2
b2 = fonk2()
print(b2)