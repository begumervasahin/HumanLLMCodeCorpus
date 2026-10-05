def get_prime():
    while True:
        try:
            a_number = input("Please enter a number: ")
            proper_number = int(a_number)
            return proper_number
        except ValueError:
            print("The value entered is not an integer")
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for element in range(2, number
            if number % element == 0:
                return False
        return True
def get_range():
    print("Provide a range of numbers to find out which ones are prime.")
    first_number = get_prime()
    second_number = get_prime()
    prime_list = range_of_prime(first_number, second_number)
    return prime_list
def range_of_prime(num1, num2):
    list_of_primes = []
    for element in range(num1, num2 + 1):
        if is_prime(element):
            list_of_primes.append(element)
    return list_of_primes
def next_hundred_primes(number):
    list_of_primes = []
    prime_start = number + 1
    while len(list_of_primes) < 100:
        if is_prime(prime_start):
            list_of_primes.append(prime_start)
        prime_start += 1
    return list_of_primes
if __name__ == "__main__":
    user_number = get_prime()
    print(user_number)
    if is_prime(user_number):
        print(f"{user_number} is a prime number")
    else:
        print(f"{user_number} is not a prime number")
    print()
    prime_range = get_range()
    print(f"The list of prime numbers in the range are {prime_range}")
    print()
    next_hundred = next_hundred_primes(user_number)
    print(f"The next 100 prime numbers after {user_number} are {next_hundred}")