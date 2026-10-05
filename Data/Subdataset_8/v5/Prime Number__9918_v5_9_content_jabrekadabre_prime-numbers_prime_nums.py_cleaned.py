def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def main():
    a = int(input("Enter the value of 'a': "))
    if is_prime(a):
        print("The given number is prime.")
    else:
        print("The given number is not prime.")
if __name__ == "__main__":
    main()