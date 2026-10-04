import random
import math
def estimate_pi(n_throws):
    inside = 0
    for _ in range(n_throws):
        if math.hypot(random.random(), random.random()) < 1:
            inside += 1
    return 4.0 * inside / n_throws
for n in [10**4, 10**6, 10**7, 10**8]:
    print(f"{n:9d}: {estimate_pi(n):.7f}")