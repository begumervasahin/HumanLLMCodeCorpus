def check_if_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
if __name__ == '__main__':
    user_input = int(input("Enter the value of a: "))
    if check_if_prime(user_input):
        print("The given number is a prime.")
    else:
        print("The given number is not a prime.")