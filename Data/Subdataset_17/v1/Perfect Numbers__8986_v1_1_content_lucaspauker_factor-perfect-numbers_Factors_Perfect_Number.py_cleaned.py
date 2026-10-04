def s(n):
    numsum = 0
    factors = []
    x = 1
    while x <= (n + 1)
        if n % x == 0:
            numsum += x
            factors.append(x)
        x += 1
    print('Factors:', factors)
    print('Sum of factors:', numsum)
    print('Number of factors:', len(factors))
    if numsum == n:
        return 'Perfect'
    elif numsum < n:
        return 'Deficient'
    else:
        return 'Abundant'
def squares(n):
    factors = []
    x = 1
    while x <= (n + 1)
        y = x ** 2
        if n % y == 0:
            factors.append(x)
        x += 1
    print('Perfect square factors:', factors)
    print('Number of perfect square factors:', len(factors))
n = 28
print(s(n))
squares(n)