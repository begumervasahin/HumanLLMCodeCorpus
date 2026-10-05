from timeit import default_timer
def get_prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor != 0:
            divisor += 1
        else:
            n
            factors.append(divisor)
    if n > 1:
        factors.append(n)
    return factors
def solve_problem_12():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    start_time = default_timer()
    n = 500 * 2
    while True:
        triangle_number = (n * (n + 1))
        prime_factors = get_prime_factors(triangle_number)
        factor_count = 1
        for factor in set(prime_factors):
            factor_count *= (prime_factors.count(factor) + 1)
        if factor_count > 500:
            break
        n += 1
    end_time = default_timer()
    execution_time = (end_time - start_time) * 1000
    print("   Triangle Number x with over 500 factors:   %d" % triangle_number)
    print("   Computation Time:                          %.3fms" % execution_time)
if __name__ == '__main__':
    solve_problem_12()