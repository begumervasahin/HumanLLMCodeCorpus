def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def main():
    try:
        number = int(input("Please enter an integer you want to check: "))
        if is_prime(number):
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()