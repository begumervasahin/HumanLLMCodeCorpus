def get_prime():
    while True:
        a_number = input("Please enter a number: ")
        try:
            return int(a_number)
        except ValueError:
            print("The value entered is not an integer. Please try again.")
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True
def get_range():
    print("Provide a range of numbers to find out which numbers are prime numbers.")
    first_number = get_prime()
    second_number = get_prime()
    return range_of_prime(min(first_number, second_number), max(first_number, second_number))
def range_of_prime(num1, num2):
    return [element for element in range(num1, num2 + 1) if is_prime(element)]
def next_hundred_primes(number):
    primes = []
    prime_candidate = number
    while len(primes) < 100:
        prime_candidate += 1
        if is_prime(prime_candidate):
            primes.append(prime_candidate)
    return primes
if __name__ == "__main__":
    user_number = get_prime()
    if is_prime(user_number):
        print(f"{user_number} is a Prime")
    else:
        print(f"{user_number} is not a Prime")
    prime_range = get_range()
    print(f"The list of primes in the given range is: {prime_range}")
    one_hundred_primes = next_hundred_primes(user_number)
    print(f"The list of the next 100 primes after {user_number} is: {one_hundred_primes}")