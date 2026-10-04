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
        start_range = primes[prime_index - 1]**2 if prime_index else current_prime + 1
        primes.extend(i for i in range(start_range, current_prime**2) if state[i] == 0)
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
    start_time = time.time()
    result = wsieve(N)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Finding primes up to {N} took {duration:.4f} seconds")
    db.ensure(result)
if __name__ == "__main__":
    go()