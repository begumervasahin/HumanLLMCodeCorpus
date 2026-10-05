def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer.")
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def find_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes
def find_next_hundred_primes(start):
    primes = []
    num = start + 1
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
if __name__ == "__main__":
    user_number = get_integer_input("Please enter a number: ")
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")
    print()
    print("Enter the range of numbers to find prime numbers within it:")
    start_number = get_integer_input("Enter the start of the range: ")
    end_number = get_integer_input("Enter the end of the range: ")
    primes_in_range = find_primes_in_range(start_number, end_number)
    print(f"The prime numbers in the range [{start_number}, {end_number}] are: {primes_in_range}")
    print()
    next_hundred = find_next_hundred_primes(user_number)
    print(f"The next 100 prime numbers after {user_number} are: {next_hundred}")