import db
import itertools
import time
def wsieve(N):
    state = [-1, -1] + [0] * (N - 1)
    primes = [2]
    prime_i = 0
    lcm = 1
    p = 2
    while p ** 2 < N:
        primes.extend(i for i in range(state.index(0, primes[-1] + 1), p ** 2) if state[i] == 0)
        if lcm < p ** 2:
            composite_range = itertools.chain([1], (i for i in range(p, min(lcm, N
        else:
            composite_range = itertools.chain([1], primes[prime_i:], (i for i in range(p ** 2, min(lcm, N
        next_lcm = p * lcm
        for sortaprime in composite_range:
            for i in range(p * sortaprime, N + 1, next_lcm):
                state[i] = p
        lcm = next_lcm
        prime_i += 1
        p = primes[prime_i]
    return primes
def go():
    N = int(10 ** 6)
    t0 = time.time()
    r = wsieve(N)
    t1 = time.time()
    print(f"For N = {N}, the algorithm took {t1 - t0:.4f} seconds.")
    db.ensure(r)
go()