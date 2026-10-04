import random
import math
def fonk1(n_throws):
    a1 = 0
    for _ in range(n_throws):
        x, b1 = random.random(), random.random()
        if math.hypot(x, b1) < 1:
            a1 += 1
    b2 = 4.0 * a1 / n_throws
    return b2
def fonk2():
    for n in [10**4, 10**5, 10**6, 10**7]:
        b2 = fonk1(n)
        print(f"Throws: {n:9d}, Estimated Pi: {b2:.7f}")
if b3 = = "__main__":
    fonk2()