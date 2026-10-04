def get_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("The value entered is not an integer. Please enter a valid integer.")
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True
def get_prime_range():
    print("Provide a range of numbers to find out which numbers in the range are prime numbers.")
    first_number = get_integer("Enter the first number: ")
    second_number = get_integer("Enter the second number: ")
    lower, upper = sorted([first_number, second_number])
    return find_primes_in_range(lower, upper)
def find_primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]
def find_next_hundred_primes(start_number):
    primes = []
    candidate = start_number + 1
    while len(primes) < 100:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes
if __name__ == "__main__":
    user_number = get_integer("Please enter a number: ")
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")
    print("\n")
    primes_in_range = get_prime_range()
    print(f"The list of primes in the range is: {primes_in_range}")
    print("\n")
    next_hundred_primes = find_next_hundred_primes(user_number)
    print(f"The next 100 prime numbers after {user_number} are: {next_hundred_primes}")