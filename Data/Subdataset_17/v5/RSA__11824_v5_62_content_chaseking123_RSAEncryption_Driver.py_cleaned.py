import py_compile
import sys
from RSA import *
import py_compile
sys.setrecursionlimit(10000000)
py_compile.compile('Driver.py')
def main():
    while True:
        try:
            option = int(input("Input 1-4 from the following options:\n"
                               "1: Check for primality\n"
                               "2: Generate a prime\n"
                               "3: Encrypt a message\n"
                               "4: Quit\n"
                               "Enter your choice: "))
            if 1 <= option <= 4:
                print(f"You chose option {option}")
                problem_selector(option)
                if option == 4:
                    break
            else:
                print("Invalid Option, you need to type 1, 2, 3, or 4.")
        except ValueError:
            print("Please enter an integer.")
def problem_selector(option):
    if option == 1:
        check_primality()
    elif option == 2:
        generate_prime()
    elif option == 3:
        encrypt_message()
    elif option == 4:
        print("Exiting...")
        exit()
def check_primality():
    N = get_positive_integer("Choose an input N to check for primality (must be positive): ")
    K = get_positive_integer("Choose K amount of times you want it tested (must be positive): ")
    is_prime = primality3(N, K)
    print(f"Is the number prime? {is_prime}")
def generate_prime():
    N = get_positive_integer("Choose an input size N to make a binary prime number of N bits (must be positive): ")
    K = get_positive_integer("Choose K amount of times you want it tested (must be positive): ")
    prime_num = generatePrime(N, K)
    print(f"Generated prime number: {prime_num}")
def encrypt_message():
    N = get_positive_integer("Choose an input N to make a prime number of N bits (must be positive, larger input required for encryption of longer messages): ")
    K = get_positive_integer("Choose K amount of times you want it tested for primality (must be positive): ")
    M = input("Choose a string or integer M to be encrypted: ")
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