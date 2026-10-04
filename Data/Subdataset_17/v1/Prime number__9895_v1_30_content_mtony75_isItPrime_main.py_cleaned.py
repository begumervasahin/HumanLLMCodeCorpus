def is_it_valid(number):
    try:
        int(number)
        return True
    except ValueError:
        print("User Input is not an integer")
        return False
def is_a_prime(number):
    if number < 2:
        print(f"{number} is not a prime number")
        return False
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            return False
    print(f"{number} is a prime number")
    return True
while True:
    user_input = input("Enter a number (or type 'stop' to end): ")
    if user_input.lower() == 'stop':
        break
    if is_it_valid(user_input):
        is_a_prime(int(user_input))