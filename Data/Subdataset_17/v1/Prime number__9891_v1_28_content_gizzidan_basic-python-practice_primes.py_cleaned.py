def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def main():
    bound_1 = int(input("Enter first number: "))
    bound_2 = int(input("Enter second number: "))
    bounds = [bound_1, bound_2]
    bounds.sort()
    primes = [x for x in range(bounds[0] + 1, bounds[1]) if is_prime(x)]
    if len(primes) > 1:
        for i in range(0, len(primes) - 1, 3):
            primes[i] = str(primes[i]) + ":"
        for i in range(1, len(primes) - 1, 3):
            primes[i] = str(primes[i]) + "!"
        for i in range(2, len(primes) - 1, 3):
            primes[i] = str(primes[i]) + ","
        print("".join(map(str, primes)))
    elif len(primes) == 1:
        print("".join(map(str, primes)))
    else:
        print("No Primes")
if __name__ == "__main__":
    main()