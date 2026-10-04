from timeit import default_timer
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def problem_12():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    start_time = default_timer()
    n = 500 * 2
    while True:
        t = (n * (n + 1))
        prime_factors = get_prime_factors(t)
        tally = 1
        for x in set(prime_factors):
            tally *= (prime_factors.count(x) + 1)
        if tally > 500:
            break
        n += 1
    end_time = default_timer()
    execution_time = (end_time - start_time) * 1000
    print(f"   Triangle Number with over 500 factors:   {t}")
    print(f"   Computation Time:                          {execution_time:.3f}ms")
if __name__ == '__main__':
    problem_12()