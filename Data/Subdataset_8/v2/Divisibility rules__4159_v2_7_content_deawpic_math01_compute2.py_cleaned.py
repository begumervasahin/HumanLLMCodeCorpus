
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def generate_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]
def generate_squares(prime_list, limit):
    squares = [1]
    len_primes = len(prime_list)
    for i in range(len_primes):
        square = prime_list[i] * prime_list[i]
        if square < limit:
            squares.append(square)
            for j in range(i, len_primes):
                product = prime_list[i] * prime_list[j]
                if product < limit:
                    squares.append(product)
                else:
                    break
        else:
            break
    return squares
primes = generate_primes(9, 200)
squares_products = generate_squares(primes, 201)
combined_list = primes + squares_products
combined_list.sort()
print("Combined list of primes, squares, and products:", combined_list)
print("Sorted list of prime numbers:", primes)
print("Number of prime numbers generated:", len(primes))