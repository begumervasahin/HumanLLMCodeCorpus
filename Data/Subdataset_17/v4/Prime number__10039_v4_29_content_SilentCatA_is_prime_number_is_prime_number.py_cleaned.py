def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def main():
    while True:
        user_input = input('Enter a number (or "q" to quit): ')
        if user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            prime_status = is_prime(number)
            print(f'{number} is prime: {prime_status}')
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
if __name__ == "__main__":
    main()