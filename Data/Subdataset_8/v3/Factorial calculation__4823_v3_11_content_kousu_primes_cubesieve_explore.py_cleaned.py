import math
def sieve_of_atkin(limit):
    primes = [2, 3, 5]
    is_prime = [False] * (limit + 1)
    is_prime[2], is_prime[3], is_prime[5] = True, True, True
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n1 = (4 * x**2) + (y**2)
            n2 = (3 * x**2) + (y**2)
            n3 = (3 * x**2) - (y**2)
            if n1 <= limit and (n1 % 12 == 1 or n1 % 12 == 5):
                is_prime[n1] = not is_prime[n1]
            if n2 <= limit and n2 % 12 == 7:
                is_prime[n2] = not is_prime[n2]
            if x > y and n3 <= limit and n3 % 12 == 11:
                is_prime[n3] = not is_prime[n3]
    for prime in range(5, int(math.sqrt(limit)) + 1):
        if is_prime[prime]:
            for k in range(prime**2, limit + 1, prime**2):
                is_prime[k] = False
    for num in range(7, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes
if __name__ == "__main__":
    limit = 15000
    prime_numbers = sieve_of_atkin(limit)
    print("Prime numbers up to", limit, ":", prime_numbers)