def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def main():
    try:
        mynum = int(input("Please enter an integer you want to check: "))
        if check_prime(mynum):
            print(f"{mynum} is a prime number")
        else:
            print(f"{mynum} is not a prime number")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()