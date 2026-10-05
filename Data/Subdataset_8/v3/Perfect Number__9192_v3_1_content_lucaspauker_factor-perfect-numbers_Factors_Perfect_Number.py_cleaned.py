def sum_of_factors(n):
    num_sum = 0
    factors = []
    for x in range(1, n
        if n % x == 0:
            num_sum += x
            factors.append(x)
    return num_sum, factors
def classify_number(n):
    num_sum, _ = sum_of_factors(n)
    if num_sum == n:
        return 'Perfect'
    elif num_sum < n:
        return 'Deficient'
    else:
        return 'Abundant'
def perfect_square_factors(n):
    factors = [x for x in range(1, n
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