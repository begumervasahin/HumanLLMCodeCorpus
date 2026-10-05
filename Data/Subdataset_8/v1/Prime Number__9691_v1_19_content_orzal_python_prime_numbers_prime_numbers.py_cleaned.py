def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
for n in range(2, 100):
    if is_prime(n):
        print(n, 'is a prime number')
    else:
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n
                break