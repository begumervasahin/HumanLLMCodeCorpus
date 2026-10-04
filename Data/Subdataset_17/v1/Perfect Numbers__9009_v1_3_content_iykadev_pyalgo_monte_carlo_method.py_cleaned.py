import random
import math
def pi(nthrows):
    inside = 0
    for i in range(nthrows):
        if math.hypot(random.random(), random.random()) < 1:
            inside += 1
    return 4.0 * inside / nthrows
def main():
    nthrows_list = [10**4, 10**6, 10**7, 10**8]
    for n in nthrows_list:
        estimated_pi = pi(n)
        print(f"{n:9d}: {estimated_pi:.7f}")
if __name__ == "__main__":
    main()