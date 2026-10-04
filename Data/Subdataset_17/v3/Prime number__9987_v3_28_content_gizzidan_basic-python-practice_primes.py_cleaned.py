def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def format_primes(primes):
    for i in range(0, len(primes), 3):
        primes[i] = f"{primes[i]}:"
    for i in range(1, len(primes), 3):
        primes[i] = f"{primes[i]}!"
    for i in range(2, len(primes), 3):
        primes[i] = f"{primes[i]},"
    return primes
def main():
    try:
        bound_1 = int(input("Enter first number: "))
        bound_2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    lower_bound, upper_bound = sorted([bound_1, bound_2])
    primes = [x for x in range(lower_bound + 1, upper_bound) if is_prime(x)]
    if primes:
        formatted_primes = format_primes(primes)
        print("".join(formatted_primes))
    else:
        print("No Primes")
if __name__ == "__main__":
    main()