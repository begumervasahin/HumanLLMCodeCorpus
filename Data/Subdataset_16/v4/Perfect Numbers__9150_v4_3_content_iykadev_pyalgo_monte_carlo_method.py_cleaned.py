import random
import math
def fonk1(n_throws):
    a1 = 0
    for _ in range(n_throws):
        if math.hypot(random.random(), random.random()) < 1:
            a1 += 1
    return 4.0 * a1 / n_throws
for n in [10**4, 10**6, 10**7, 10**8]:
    print(f"{n:9d}: {fonk1(n):.7f}")