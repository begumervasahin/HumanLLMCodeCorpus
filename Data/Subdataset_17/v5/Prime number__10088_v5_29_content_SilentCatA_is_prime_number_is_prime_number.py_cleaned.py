def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def main():
    while True:
        user_input = input('Enter a number (or "q" to quit): ')
        if user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            if is_prime(number):
                print(f"{number} is a prime number")
            else:
                print(f"{number} is not a prime number")
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
if __name__ == "__main__":
    main()