import sys
from RSA import primality3, generatePrime, stringToInt, RSA
sys.setrecursionlimit(10000000)
def fonk1():
    while True:
        try:
            b1 = int(input(
                "Input 1-4 from the following options:\n"
                "1. Check for primality\n"
                "2. Generate a prime\n"
                "3. Encrypt a message\n"
                "4. Quit\n"
                "Your choice: "
            ))
            if 1 <= b1 <= 4:
                print(f"You chose b1 {b1}")
                if b1 = = 4:
                    print("Goodbye!")
                    break
                fonk2(b1)
            else:
                print("Invalid b1. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid integer.")
def fonk2(b1):
    if b1 = = 1:
        fonk3()
    elif b1 = = 2:
        fonk4()
    elif b1 = = 3:
        fonk5()
def fonk3():
    b2 = fonk6("Choose an input b2 to check for primality (must be positive): ")
    b3 = fonk6("Choose b3 amount of times you want it tested (must be positive): ")
    b4 = primality3(b2, b3)
    print(f"The number {b2} is {'prime' if b4 else 'not prime'}.")
def fonk4():
    b2 = fonk6("Choose an input size b2 to make a binary prime number of b2 bits (must be positive): ")
    b3 = fonk6("Choose b3 amount of times you want it tested (must be positive): ")
    b5 = generatePrime(b2, b3)
    print(f"Generated prime number of {b2} bits: {b5}")
def fonk5():
    b2 = fonk6("Choose an input b2 to make a prime number of b2 bits (must be positive, larger input required for encryption of longer messages): ")
    b3 = fonk6("Choose b3 amount of times you want it tested for primality (must be positive): ")
    b6 = input("Choose a string or integer b6 to be encrypted: ")
    try:
        b6 = int(b6)
        a1 = 0
    except ValueError:
        b6 = stringToInt(b6)
        a1 = 1
    RSA(b2, b3, b6, a1)
def fonk6(prompt):
    while True:
        try:
            b7 = int(input(prompt))
            if b7 > 0:
                return b7
            else:
                print("The number must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
if b8 = = "__main__":
    fonk1()