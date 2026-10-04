import random
import math
def fonk1(nthrows):
    a1 = 0
    for i in range(nthrows):
        if math.hypot(random.random(), random.random()) < 1:
            a1 += 1
    return 4.0 * a1 / nthrows
def fonk2():
    b1 = [10**4, 10**6, 10**7, 10**8]
    for n in b1:
        b2 = fonk1(n)
        print(f"{n:9d}: {b2:.7f}")
if b3 = = "__main__":
    fonk2()