import itertools
import time
import db
def wsieve(N):
    state = [-1, -1] + [0] * (N - 1)
    primes = [2]
    prime_index = 0
    lcm = 1
    current_prime = 2
    while current_prime**2 < N:
        primes.extend(i for i in range(state.index(0, primes[-1] + 1), current_prime**2) if state[i] == 0)
        if lcm < current_prime**2:
            U = itertools.chain([1], (i for i in range(current_prime, min(lcm, N
        else:
            U = itertools.chain([1], primes[prime_index:], (i for i in range(current_prime**2, min(lcm, N
        next_lcm = current_prime * lcm
        for sortaprime in U:
            for i in range(current_prime * sortaprime, N + 1, next_lcm):
                state[i] = current_prime
        lcm = next_lcm
        prime_index += 1
        current_prime = primes[prime_index]
    return primes
def go():
    N = int(10**6)
    t0 = time.time()
    result = wsieve(N)
    t1 = time.time()
    print(f"for {N} took {t1-t0:.4f} seconds")
    db.ensure(result)
if __name__ == "__main__":
    go()