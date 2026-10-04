def is_prime(x):
    if x < 2:
        return None
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return None
    return x
def generate_prime_products():
    primes = list(filter(None, map(is_prime, range(9, 201))))
    products = [1]
    for i, prime_i in enumerate(primes):
        square = prime_i * prime_i
        if square < 201:
            products.append(square)
            for j in range(i + 1, len(primes)):
                product = prime_i * primes[j]
                if product < 201:
                    products.append(product)
                else:
                    break
        else:
            break
    all_numbers = sorted(set(primes + products))
    return all_numbers
def main():
    result = generate_prime_products()
    print(result)
if __name__ == "__main__":
    main()