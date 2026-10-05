def calculate_sum_of_factors(n):
    num_sum = 0
    factors = []
    for x in range(1, (n
        if n % x == 0:
            num_sum += x
            factors.append(x)
    return num_sum, factors
def classify_number(n):
    num_sum, factors = calculate_sum_of_factors(n)
    if num_sum == n:
        return 'Perfect'
    elif num_sum < n:
        return 'Deficient'
    else:
        return 'Abundant'
def find_perfect_square_factors(n):
    factors = [x for x in range(1, (n
    return factors
def main():
    n = int(input("Enter a number: "))
    num_type = classify_number(n)
    print('Number:', n)
    print('Number type:', num_type)
    num_sum, factors = calculate_sum_of_factors(n)
    print('Factors:', factors)
    print('Sum of factors:', num_sum)
    print('Number of factors:', len(factors))
    if num_type == 'Deficient':
        perfect_square_factors = find_perfect_square_factors(n)
        print('Perfect square factors:', perfect_square_factors)
        print('Number of perfect square factors:', len(perfect_square_factors))
if __name__ == '__main__':
    main()