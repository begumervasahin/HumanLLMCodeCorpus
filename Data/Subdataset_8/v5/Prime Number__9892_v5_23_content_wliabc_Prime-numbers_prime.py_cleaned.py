def check_prime_number(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
if __name__ == "__main__":
    mynum = int(input("Please enter an integer you want to check: "))
    is_prime = check_prime_number(mynum)
    if is_prime:
        print(str(mynum) + " is a prime number")
    else:
        print(str(mynum) + " is not a prime number")