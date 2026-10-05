def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    while True:
        user_input = input('Enter a number (type "q" to quit): ')
        if user_input.lower() == 'q':
            break
        else:
            n = int(user_input)
            prime = is_prime(n)
            print(f'{n} is prime: {prime}')