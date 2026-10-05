import db
import itertools
import time
def wheel_sieve(limit):
    state = [-1, -1] + [0] * (limit - 1)
    primes = [2]
    prime_index = 0
    lcm = 1
    prime = 2
    while prime ** 2 < limit:
        primes.extend(i for i in range(state.index(0, primes[-1] + 1), prime ** 2) if state[i] == 0)
        if lcm < prime ** 2:
            chain_U = itertools.chain([1], [i for i in range(prime, min(lcm, limit
        else:
            chain_U = itertools.chain([1], primes[prime_index:], (i for i in range(prime ** 2, min(lcm, limit
        next_lcm = prime * lcm
        for sortaprime in chain_U:
            for i in range(prime * sortaprime, limit + 1, next_lcm):
                state[i] = prime
        lcm = next_lcm
        prime_index += 1
        prime = primes[prime_index]
    return primes
def run_wheel_sieve():
    limit = int(10 ** 6)
    start_time = time.time()
    result = wheel_sieve(limit)
    end_time = time.time()
    print(f"The wheel sieve algorithm took {end_time - start_time:.4f} seconds for {limit}.")
    db.ensure(result)
run_wheel_sieve()