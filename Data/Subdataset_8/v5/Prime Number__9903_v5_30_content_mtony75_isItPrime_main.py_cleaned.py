def is_valid_input(number):
    try:
        int(number)
        return True
    except ValueError:
        print("User Input Not an Integer")
        return False
def is_prime(number):
    if number < 2:
        print(str(number) + ' is not a prime number')
        return False
    for loop_number in range(2, int(number**0.5) + 1):
        if number % loop_number == 0:
            print(str(number) + ' is not a prime number')
            return False
    print(str(number) + ' is a prime number')
    return True
user_input = ""
while user_input != "stop":
    user_input = input("Enter a Number: ")
    if is_valid_input(user_input):
        is_prime(int(user_input))