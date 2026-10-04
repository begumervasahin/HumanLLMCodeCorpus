from timeit import default_timer
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def count_divisors(prime_factors):
    divisor_count = 1
    for factor in set(prime_factors):
        divisor_count *= prime_factors.count(factor) + 1
    return divisor_count
def find_highly_divisible_triangular_number(divisor_limit):
    n = 1
    while True:
        triangle_number = n * (n + 1)
        prime_factors = get_prime_factors(triangle_number)
        if count_divisors(prime_factors) > divisor_limit:
            return triangle_number
        n += 1
def problem_12():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    start_time = default_timer()
    divisor_limit = 500
    result = find_highly_divisible_triangular_number(divisor_limit)
    end_time = default_timer()
    execution_time = (end_time - start_time) * 1000
    print(f"   Triangle Number with over {divisor_limit} factors: {result}")
    print(f"   Computation Time: {execution_time:.3f} ms")
if __name__ == '__main__':
    problem_12()