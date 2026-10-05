def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input_int = int(user_input)
            return user_input_int
        except ValueError:
            print("Please enter an integer.")
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for divisor in range(2, number
            if number % divisor == 0:
                return False
        return True
def get_prime_range():
    print("Provide a range of numbers to find out which ones are prime.")
    first_number = get_integer_input("Enter the starting number: ")
    second_number = get_integer_input("Enter the ending number: ")
    prime_list = find_primes_in_range(first_number, second_number)
    return prime_list
def find_primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
def find_next_hundred_primes(number):
    primes_after_number = []
    next_number = number + 1
    while len(primes_after_number) < 100:
        if is_prime(next_number):
            primes_after_number.append(next_number)
        next_number += 1
    return primes_after_number
if __name__ == "__main__":
    user_input_number = get_integer_input("Please enter a number: ")
    print(user_input_number)
    if is_prime(user_input_number):
        print(f"{user_input_number} is a prime number")
    else:
        print(f"{user_input_number} is not a prime number")
    print()
    prime_range = get_prime_range()
    print(f"The list of prime numbers in the range are {prime_range}")
    print()
    next_hundred = find_next_hundred_primes(user_input_number)
    print(f"The next 100 prime numbers after {user_input_number} are {next_hundred}")