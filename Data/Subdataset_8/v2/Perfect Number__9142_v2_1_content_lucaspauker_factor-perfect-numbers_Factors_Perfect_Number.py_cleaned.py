def sum_of_factors(n):
    numsum = 0
    factors = []
    x = 1
    while x <= (n + 1) / 2:
        if n % x == 0:
            numsum += x
            factors.append(x)
        x += 1
    return numsum, factors
def classify_number(n):
    numsum, _ = sum_of_factors(n)
    if numsum == n:
        return 'Perfect'
    elif numsum < n:
        return 'Deficient'
    else:
        return 'Abundant'
def perfect_square_factors(n):
    factors = []
    x = 1
    while x <= (n + 1) / 2:
        y = x ** 2
        if n % y == 0:
            factors.append(x)
        x += 1
    return factors
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Classifying number...")
    classification = classify_number(number)
    print(f"Classification: {classification}")
    if classification in ['Perfect', 'Deficient']:
        factors_sum, factors = sum_of_factors(number)
        print(f"Factors: {factors}")
        print(f"Sum of factors: {factors_sum}")
        print(f"Number of factors: {len(factors)}")
    else:
        perfect_sq_factors = perfect_square_factors(number)
        print(f"Perfect square factors: {perfect_sq_factors}")
        print(f"Number of perfect square factors: {len(perfect_sq_factors)}")