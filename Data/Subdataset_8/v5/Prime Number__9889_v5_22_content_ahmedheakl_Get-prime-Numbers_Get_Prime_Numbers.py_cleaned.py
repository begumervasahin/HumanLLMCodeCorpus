def get_prime_numbers(end_range):
    prime_numbers = []
    for i in range(1, end_range):
        sqrt_value = (24 * i + 1) ** 0.5
        if sqrt_value % 1 == 0 and int(sqrt_value) < end_range:
            prime_numbers.append(int(sqrt_value))
        elif int(sqrt_value) > end_range:
            break
    prime_numbers = [num for num in prime_numbers if all(num % i != 0 for i in range(2, 10))]
    prime_squares = [num ** 2 for num in prime_numbers]
    prime_numbers = [num for num in prime_numbers if num not in prime_squares]
    prime_numbers.extend([2, 3, 5, 7])
    prime_numbers.sort()
    return prime_numbers
if __name__ == "__main__":
    end_range = int(input('Enter the end of the range: '))
    primes = get_prime_numbers(end_range)
    print(primes)