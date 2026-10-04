def eratosthenes(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))
def main():
    limit = 100
    primes = list(eratosthenes(limit))
    print(primes)
if __name__ == "__main__":
    main()