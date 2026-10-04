import time
def factors(num):
    prime_factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            prime_factors.append(i)
            num = num
        else:
            i += 1
    print(f"Prime factors: {prime_factors}")
    print(f"Number of prime factors: {len(prime_factors)}, Sum of prime factors: {sum(prime_factors)}")
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
    all_factors = set(prime_factors).union(additional_factors)
    return [1] + sorted(all_factors)
if __name__ == '__main__':
    start_time = time.time()
    result = factors(33550336)
    print(f"Factors: {result}")
    print(f"Execution time: {time.time() - start_time} seconds")