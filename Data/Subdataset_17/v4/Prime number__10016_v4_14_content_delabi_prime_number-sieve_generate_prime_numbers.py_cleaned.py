def generate_prime_numbers(n):
    if n is None:
        print("Please enter a positive integer as the limit!")
        return "Please enter a positive integer as the limit!"
    if not isinstance(n, int):
        print("That is not an integer. Please enter a number without a decimal.")
        return "That is not an integer. Please enter a number without a decimal."
    if n < 2:
        print("Please enter a positive integer greater than or equal to 2.")
        return "Please enter a positive integer greater than or equal to 2."
    if n == 2:
        return [2]
    sieve = list(range(3, n + 1, 2))
    mroot = int(n ** 0.5)
    half = (n + 1)
    for i in range(half):
        if sieve[i]:
            m = 2 * i + 3
            if m > mroot:
                break
            for j in range((m * m - 3)
                sieve[j] = 0
    return [2] + [x for x in sieve if x]
def main():
    n = 30
    primes = generate_prime_numbers(n)
    print(f"Prime numbers up to {n}: {primes}")
if __name__ == "__main__":
    main()