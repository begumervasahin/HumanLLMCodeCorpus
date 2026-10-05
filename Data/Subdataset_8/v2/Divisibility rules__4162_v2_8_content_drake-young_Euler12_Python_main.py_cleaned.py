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
def solve_problem_12():
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
    print("   Triangle Number x with over 500 factors:   %d" % t)
    print("   Computation Time:                          %.3fms" % execution_time)
if __name__ == '__main__':
    solve_problem_12()