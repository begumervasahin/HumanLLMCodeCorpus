def find_primes_between(bounds):
    lower_bound, upper_bound = sorted(bounds)
    primes = []
    for num in range(lower_bound + 1, upper_bound):
        if num > 1 and all(num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    if not primes:
        return "No Primes"
    formatted_primes = []
    for i, prime in enumerate(primes):
        if i % 3 == 0:
            formatted_primes.append(f"{prime}:")
        elif i % 3 == 1:
            formatted_primes.append(f"{prime}!")
        else:
            formatted_primes.append(f"{prime},")
    return "".join(formatted_primes)
def main():
    try:
        bound_1 = int(input("Enter first number: "))
        bound_2 = int(input("Enter second number: "))
        bounds = [bound_1, bound_2]
        result = find_primes_between(bounds)
        print(result)
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()