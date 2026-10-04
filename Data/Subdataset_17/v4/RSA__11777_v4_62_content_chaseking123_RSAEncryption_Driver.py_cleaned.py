import py_compile
import sys
from RSA import *
import py_compile
sys.setrecursionlimit(10000000)
py_compile.compile('Driver.py')
def main():
    try:
        option = int(input("Input 1-4 from the following options:\n"
                           "1: Check for primality\n"
                           "2: Generate a prime\n"
                           "3: Encrypt a message\n"
                           "4: Quit\n"
                           "Enter your choice: "))
        print(f"You chose option {option}")
    except ValueError:
        print("Please enter an integer.")
        main()
        return
    if 1 <= option <= 4:
        problem_selector(option)
    else:
        print("Invalid Option, you needed to type 1, 2, 3, or 4.")
        main()
def problem_selector(option):
    if option == 1:
        problem1()
    elif option == 2:
        problem2()
    elif option == 3:
        problem3()
    elif option == 4:
        exit()
def problem1():
    N = get_positive_integer("Choose an input N to check for primality (must be positive): ")
    K = get_positive_integer("Choose K amount of times you want it tested (must be positive): ")
    is_prime = primality3(N, K)
    print(f"Is the number prime? {is_prime}")
def problem2():
    N = get_positive_integer("Choose an input size N to make binary prime number of N bits (must be positive): ")
    K = get_positive_integer("Choose K amount of times you want it tested (must be positive): ")
    prime_num = generatePrime(N, K)
    print(f"Generated prime number: {prime_num}")
    main()
def problem3():
    N = get_positive_integer("Choose an input N to make prime number of N bits (must be positive, larger input required for encryption of longer messages): ")
    K = get_positive_integer("Choose K amount of times you want it tested for primality (must be positive): ")
    M = input("Choose string or integer M to be encrypted: ")
    try:
        M = int(M)
        string_flag = 0
    except ValueError:
        M = stringToInt(M)
        string_flag = 1
    RSA(N, K, M, string_flag)
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("The number must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
if __name__ == "__main__":
    main()