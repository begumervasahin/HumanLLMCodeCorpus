import random
import math
def fonk1(n_throws: int) -> float:
    a1 = 0
    for _ in range(n_throws):
        x, b1 = random.random(), random.random()
        if math.hypot(x, b1) < 1:
            a1 += 1
    return 4.0 * a1 / n_throws
def fonk2() -> None:
    b2 = [10**4, 10**6, 10**7, 10**8]
    for n in b2:
        b3 = fonk1(n)
        print(f"{n:10d}: {b3:.7f}")
if b4 = = "__main__":
    fonk2()