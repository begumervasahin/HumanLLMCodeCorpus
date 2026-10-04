def sieve_of_eratosthenes(limit: int):
    multiples = set()
    for number in range(2, limit + 1):
        if number not in multiples:
            yield number
            multiples.update(range(number * number, limit + 1, number))
def main() -> None:
    primes = list(sieve_of_eratosthenes(100))
    print(primes)
if __name__ == "__main__":
    main()