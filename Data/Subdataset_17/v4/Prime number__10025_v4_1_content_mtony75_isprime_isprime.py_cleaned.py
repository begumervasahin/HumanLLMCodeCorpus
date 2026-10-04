def get_prime():
    while True:
        a_number = input("Please enter a number: ")
        try:
            proper_number = int(a_number)
            return proper_number
        except ValueError:
            print(f"The value entered is not an integer. Please enter a valid integer.")
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for element in range(2, number
        if number % element == 0:
            return False
    return True
def get_range():
    print("Provide a range of numbers to find out which numbers in the range are prime numbers.")
    first_number = get_prime()
    second_number = get_prime()
    if first_number < second_number:
        return range_of_primes(first_number, second_number)
    else:
        return range_of_primes(second_number, first_number)
def range_of_primes(num1, num2):
    list_of_primes = [element for element in range(num1, num2 + 1) if is_prime(element)]
    return list_of_primes
def next_hundred_primes(start_number):
    list_of_primes = []
    prime_start = start_number
    while len(list_of_primes) < 100:
        prime_start += 1
        if is_prime(prime_start):
            list_of_primes.append(prime_start)
    return list_of_primes
if __name__ == "__main__":
    user_number = get_prime()
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")
    print("\n")
    prime_range = get_range()
    print(f"The list of primes in the range is: {prime_range}")
    print("\n")
    one_hundred_primes = next_hundred_primes(user_number)
    print(f"The next 100 prime numbers after {user_number} are: {one_hundred_primes}")