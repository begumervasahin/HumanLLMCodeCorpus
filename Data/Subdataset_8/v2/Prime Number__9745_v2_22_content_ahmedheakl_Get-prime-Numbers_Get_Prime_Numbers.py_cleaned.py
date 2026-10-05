
end_range = int(input('Enter the end of the range: '))
prime_numbers = []
temp = 0
for i in range(1, 1000000000000000000):
    temp = (24 * i + 1) ** 0.5
    if temp % 1 == 0 and int(temp) < end_range:
        prime_numbers.append(int(temp))
    elif int(temp) > end_range:
        break
for i in range(2, 10):
    for num in prime_numbers:
        if num % i == 0:
            prime_numbers.remove(num)
squared_primes = [num ** 2 for num in prime_numbers]
for num_squared in squared_primes:
    for prime in prime_numbers:
        if prime == num_squared:
            prime_numbers.remove(prime)
initial_primes = [2, 3, 5, 7]
prime_numbers += initial_primes
sorted_primes = sorted(prime_numbers)
print(sorted_primes)