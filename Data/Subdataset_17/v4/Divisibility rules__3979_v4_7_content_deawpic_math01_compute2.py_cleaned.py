def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return None
    return x
def generate_prime_related_numbers(limit):
    primes = list(filter(None, map(is_prime, range(9, limit))))
    prime_products = [1]
    for i, prime_i in enumerate(primes):
        square = prime_i * prime_i
        if square < limit:
            prime_products.append(square)
            for j in range(i + 1, len(primes)):
                product = prime_i * primes[j]
                if product < limit:
                    prime_products.append(product)
                else:
                    break
        else:
            break
    all_numbers = sorted(set(primes + prime_products))
    return all_numbers
def main():
    result = generate_prime_related_numbers(201)
    print(result)
if __name__ == "__main__":
    main()