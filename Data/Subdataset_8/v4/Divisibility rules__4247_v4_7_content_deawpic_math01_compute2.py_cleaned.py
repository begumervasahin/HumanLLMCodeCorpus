def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True
def generate_primes(start, end):
    return [number for number in range(start, end + 1) if is_prime(number)]
def get_squares_and_products(prime_list, limit):
    squares_products = [1]
    for i in range(len(prime_list)):
        square = prime_list[i] * prime_list[i]
        if square < limit:
            squares_products.append(square)
            for j in range(i, len(prime_list)):
                product = prime_list[i] * prime_list[j]
                if product < limit:
                    squares_products.append(product)
                else:
                    break
        else:
            break
    return squares_products
primes = generate_primes(9, 200)
squares_products = get_squares_and_products(primes, 201)
combined_list = sorted(primes + squares_products)
print("Combined list:", combined_list)
print("Sorted list of primes:", primes)
print("Number of prime numbers:", len(primes))