def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def format_primes(prime_list):
    formatted_primes = []
    for i, prime in enumerate(prime_list):
        if i % 3 == 0:
            formatted_primes.append(str(prime) + ":")
        elif i % 3 == 1:
            formatted_primes.append(str(prime) + "!")
        elif i % 3 == 2:
            formatted_primes.append(str(prime) + ",")
    return formatted_primes
def main():
    bound_1 = int(input("Enter first number: "))
    bound_2 = int(input("Enter second number: "))
    bounds = [bound_1, bound_2]
    bounds.sort()
    primes = [x for x in range(bounds[0] + 1, bounds[1]) if is_prime(x)]
    if primes:
        formatted_primes = format_primes(primes)
        print("".join(formatted_primes))
    else:
        print("No Primes")
if __name__ == "__main__":
    main()