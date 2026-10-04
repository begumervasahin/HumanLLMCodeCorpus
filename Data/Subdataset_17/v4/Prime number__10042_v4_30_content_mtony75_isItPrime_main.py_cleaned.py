def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        print("User input is not a valid integer.")
        return False
def is_prime(number):
    if number <= 1:
        print(f"{number} is not a prime number.")
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            print(f"{number} is not a prime number.")
            return False
    print(f"{number} is a prime number.")
    return True
while True:
    user_input = input("Enter a number (or type 'stop' to exit): ")
    if user_input.lower() == 'stop':
        break
    if is_valid_integer(user_input):
        is_prime(int(user_input))