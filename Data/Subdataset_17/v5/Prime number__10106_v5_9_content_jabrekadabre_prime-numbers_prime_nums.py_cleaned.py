def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def main():
    try:
        number = int(input("Enter a number to check if it is prime: "))
        if is_prime(number):
            print("The given number is a prime")
        else:
            print("The given number is not a prime")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == '__main__':
    main()