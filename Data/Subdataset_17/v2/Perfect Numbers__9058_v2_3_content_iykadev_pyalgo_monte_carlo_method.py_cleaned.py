import random
import math
def estimate_pi(n_throws: int) -> float:
    inside_circle = 0
    for _ in range(n_throws):
        x, y = random.random(), random.random()
        if math.hypot(x, y) < 1:
            inside_circle += 1
    return 4.0 * inside_circle / n_throws
def main() -> None:
    n_throws_list = [10**4, 10**6, 10**7, 10**8]
    for n in n_throws_list:
        estimated_pi = estimate_pi(n)
        print(f"{n:10d}: {estimated_pi:.7f}")
if __name__ == "__main__":
    main()