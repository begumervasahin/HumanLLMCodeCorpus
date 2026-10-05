from timeit import default_timer
def get_prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n
        else:
            divisor += 1
    if n > 1:
        factors.append(n)
    return factors
def solve_problem_12():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    start_time = default_timer()
    target_factors = 500
    n = 2 * target_factors
    while True:
        triangle_number = (n * (n + 1))
        prime_factors = get_prime_factors(triangle_number)
        factors_count = 1
        for factor in set(prime_factors):
            factors_count *= (prime_factors.count(factor) + 1)
        if factors_count > target_factors:
            break
        n += 1
    end_time = default_timer()
    execution_time = (end_time - start_time) * 1000
    print("   Triangle Number x with over 500 factors:   %d" % triangle_number)
    print("   Computation Time:                          %.3fms" % execution_time)
if __name__ == '__main__':
    solve_problem_12()