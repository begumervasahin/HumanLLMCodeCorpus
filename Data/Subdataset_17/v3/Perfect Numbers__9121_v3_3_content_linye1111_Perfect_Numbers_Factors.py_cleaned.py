import time
def prime_factors(num):
    factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num = num
        else:
            i += 1
    return factors
def generate_additional_factors(prime_factors):
    additional_factors = set()
    num_prime_factors = len(prime_factors)
    for i in range(num_prime_factors):
        for j in range(i + 1, num_prime_factors):
            product = prime_factors[i] * prime_factors[j]
            additional_factors.add(product)
            temp_product = product
            for k in range(j + 1, num_prime_factors):
                temp_product *= prime_factors[k]
                additional_factors.add(temp_product)
    return additional_factors
def factors(num):
    prime_factors_list = prime_factors(num)
    print(f"Prime factors: {prime_factors_list}")
    print(f"Number of prime factors: {len(prime_factors_list)}, Sum of prime factors: {sum(prime_factors_list)}")
    additional_factors = generate_additional_factors(prime_factors_list)
    all_factors = set(prime_factors_list).union(additional_factors)
    return [1] + sorted(all_factors)
if __name__ == '__main__':
    start_time = time.time()
    result = factors(33550336)
    print(f"Factors: {result}")
    print(f"Execution time: {time.time() - start_time} seconds")