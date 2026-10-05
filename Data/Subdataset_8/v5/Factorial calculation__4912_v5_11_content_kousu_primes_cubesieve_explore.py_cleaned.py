import zns
from db import primes as RealPrimes
def sieve(N):
    primes = [2]
    state = [-1] * 2 + [0] * N
    prime_index = 0
    current_prime = 2
    upper_limit = 2
    while current_prime ** 2 < N:
        print(f" -- {current_prime} -- ")
        for i in range(primes[prime_index - 1] ** 2 if prime_index else current_prime + 1, current_prime ** 2):
            if state[i] == 0:
                print("new ^2 prime:", i)
                primes.append(i)
        print(f" -- {current_prime}**2 -- ")
        for index, prime in enumerate(primes[:prime_index]):
            lcm = zns.lcm(index)
            for i in range(upper_limit + (prime - (upper_limit % prime)), min(current_prime ** 3, N + 1), prime):
                if state[i] == 0:
                    if prime > 3:
                        print(f"  {prime}] new: {i} = {prime}*({lcm}[{(i
                state[i] = prime
            if prime > 3:
                print()
            else:
                print(f"  {prime}] ...\n")
        for prime in primes[prime_index:]:
            multiple = prime * current_prime
            if prime > current_prime ** 2:
                print(f"uh oh, breaking because while marking cubethm composites got a {prime} > {current_prime ** 2}")
                break
            if multiple > N:
                continue
            assert multiple < current_prime ** 3
            if state[multiple] == 0:
                print(f"  [{current_prime} * {prime} = {multiple}]")
            state[multiple] = current_prime
        if current_prime ** 3 < N:
            print(f"  [{current_prime}**3 = {current_prime ** 3}]")
            state[current_prime ** 3] = current_prime
        upper_limit = current_prime ** 3
        print(f" -- {current_prime}**3 -- ")
        prime_index += 1
        current_prime = primes[prime_index]
        print("-" * 22)
        assert RealPrimes[:len(primes)] == primes or len(primes) > len(RealPrimes)
sieve(15000)