def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def main():
    while True:
        user_input = input('> ').strip()
        if user_input.lower() == 'q':
            break
        try:
            n = int(user_input)
            result = is_prime(n)
            print(f'{n} is prime: {result}')
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")
if __name__ == "__main__":
    main()