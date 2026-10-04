def classify_number(n):
    total_sum = 0
    factors = []
    for x in range(1, n
        if n % x == 0:
            total_sum += x
            factors.append(x)
    print('Factors:', factors)
    print('Sum of factors:', total_sum)
    print('Number of factors:', len(factors))
    if total_sum == n:
        return 'Perfect'
    elif total_sum < n:
        return 'Deficient'
    else:
        return 'Abundant'
def find_perfect_square_factors(n):
    square_factors = []
    for x in range(1, int(n**0.5) + 1):
        if n % (x ** 2) == 0:
            square_factors.append(x)
    print('Perfect square factors:', square_factors)
    print('Number of perfect square factors:', len(square_factors))
number = 28
print(classify_number(number))
find_perfect_square_factors(number)