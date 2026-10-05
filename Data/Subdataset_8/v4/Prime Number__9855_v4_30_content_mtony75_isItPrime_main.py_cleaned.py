def is_valid_input(number):
    try:
        if int(number):
            return True
    except:
        print("User Input Not an Integer")
        return False
def is_prime(number):
    for loop_number in range(2, number):
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