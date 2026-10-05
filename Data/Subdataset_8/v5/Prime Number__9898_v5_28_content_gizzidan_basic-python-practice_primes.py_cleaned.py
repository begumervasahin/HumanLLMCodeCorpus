def find_primes(bound_1, bound_2):
    bounds = sorted([bound_1, bound_2])
    primes = []
    for num in range(bounds[0] + 1, bounds[1]):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes
def format_primes(primes):
    formatted_primes = primes[:]
    for i in range(0, len(formatted_primes) - 1, 3):
        formatted_primes[i] = str(formatted_primes[i]) + ":"
    for i in range(1, len(formatted_primes) - 1, 3):
        formatted_primes[i] = str(formatted_primes[i]) + "!"
    for i in range(2, len(formatted_primes) - 1, 3):
        formatted_primes[i] = str(formatted_primes[i]) + ","
    return formatted_primes
if __name__ == "__main__":
    bound_1 = int(input("Enter the first number: "))
    bound_2 = int(input("Enter the second number: "))
    primes = find_primes(bound_1, bound_2)
    if primes:
        formatted_primes = format_primes(primes)
        print("".join(map(str, formatted_primes)))
    else:
        print("No prime numbers found")