import random
import math
def estimate_pi(n_throws):
    inside_circle = 0
    for _ in range(n_throws):
        x, y = random.random(), random.random()
        if math.hypot(x, y) < 1:
            inside_circle += 1
    pi_estimate = 4.0 * inside_circle / n_throws
    return pi_estimate
def main():
    for n in [10**4, 10**5, 10**6, 10**7]:
        pi_estimate = estimate_pi(n)
        print(f"Throws: {n:9d}, Estimated Pi: {pi_estimate:.7f}")
if __name__ == "__main__":
    main()