def is_valid_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        print("Invalid input: Please enter an integer.")
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
def main():
    while True:
        user_input = input("Enter a Number (or 'stop' to quit): ")
        if user_input.lower() == "stop":
            print("Exiting the program.")
            break
        if is_valid_integer(user_input):
            is_prime(int(user_input))
if __name__ == "__main__":
    main()