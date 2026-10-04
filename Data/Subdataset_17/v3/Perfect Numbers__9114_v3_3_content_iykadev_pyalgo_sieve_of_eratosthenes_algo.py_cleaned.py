def sieve_of_eratosthenes(limit: int):
    multiples = set()
    for number in range(2, limit + 1):
        if number not in multiples:
            yield number
            multiples.update(range(number * number, limit + 1, number))
def main() -> None:
    limit = 100
    primes = list(sieve_of_eratosthenes(limit))
    print(f"Prime numbers up to {limit}: {primes}")
if __name__ == "__main__":
    main()