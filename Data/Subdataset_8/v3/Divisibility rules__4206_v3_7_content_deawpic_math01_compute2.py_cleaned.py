def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def generate_primes(start, end):
    primes = [number for number in range(start, end + 1) if is_prime(number)]
    return primes
def generate_squares_and_products(primes, limit):
    squares_products = [1]
    for i in range(len(primes)):
        square = primes[i] * primes[i]
        if square < limit:
            squares_products.append(square)
            for j in range(i, len(primes)):
                product = primes[i] * primes[j]
                if product < limit:
                    squares_products.append(product)
                else:
                    break
        else:
            break
    return squares_products
primes_list = generate_primes(9, 200)
squares_products_list = generate_squares_and_products(primes_list, 201)
combined_list = sorted(primes_list + squares_products_list)
print("Combined list of primes, squares, and products:", combined_list)
print("Sorted list of prime numbers:", primes_list)
print("Number of prime numbers generated:", len(primes_list))