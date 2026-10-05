def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True
if __name__ == "__main__":
    user_input = int(input("Please enter an integer you want to check: "))
    if is_prime(user_input):
        print(f"{user_input} is a prime number")
    else:
        print(f"{user_input} is not a prime number")