def generate_prime_numbers(n):
    if n is None:
        return "Error: Please enter a positive integer as the limit."
    if not isinstance(n, int):
        return "Error: The input is not an integer. Please enter a whole number."
    if n <= 0:
        return "Error: Please enter a positive integer."
    print("Starting prime number generation...")
    if n == 0:
        return [0]
    elif n == 2:
        return [2]
    elif n < 2:
        return []
    sieve = list(range(3, n + 1, 2))
    mroot = int(n ** 0.5)
    half = (n + 1)
    i = 0
    m = 3
    while m <= mroot:
        if sieve[i]:
            j = (m * m - 3)
            sieve[j] = 0
            while j < half:
                sieve[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in sieve if x]
n = 20
print(generate_prime_numbers(n))