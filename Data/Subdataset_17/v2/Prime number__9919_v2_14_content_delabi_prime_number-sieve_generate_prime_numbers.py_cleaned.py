def generate_prime_numbers(limit):
    if limit is None:
        print("Please enter a positive integer as the limit!")
        return "Please enter a positive integer as the limit!"
    if not isinstance(limit, int):
        print("That is not an integer. Please enter a number without a decimal")
        return "That is not an integer. Please enter a number without a decimal"
    if limit < 2:
        return [] if limit != 0 else [0]
    print("Hallo")
    if limit == 2:
        return [2]
    sieve = list(range(3, limit + 1, 2))
    sqrt_limit = int(limit ** 0.5)
    half_limit = (limit + 1)
    i = 0
    prime = 3
    while prime <= sqrt_limit:
        if sieve[i]:
            for j in range((prime * prime - 3)
                sieve[j] = 0
        i += 1
        prime = 2 * i + 3
    return [2] + [num for num in sieve if num]
if __name__ == "__main__":
    limit = 50
    primes = generate_prime_numbers(limit)
    print(f"Prime numbers up to {limit}: {primes}")