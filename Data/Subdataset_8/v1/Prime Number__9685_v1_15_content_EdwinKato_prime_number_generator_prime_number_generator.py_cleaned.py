def generate_prime_numbers(n):
    j = 2
    prime_numbers = []
    while j <= n:
        k = 2
        while not(k == j) and not(j % k == 0):
            k = k + 1
        if k == j:
            prime_numbers.append(j)
        j = j + 1
    return prime_numbers
result = generate_prime_numbers(10)
print(result)