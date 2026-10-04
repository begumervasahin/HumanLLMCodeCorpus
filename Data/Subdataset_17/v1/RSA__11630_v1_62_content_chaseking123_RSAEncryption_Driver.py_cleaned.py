import sys
from RSA import primality3, generatePrime, stringToInt, RSA
sys.setrecursionlimit(10000000)
def main():
    try:
        option = int(input("Input 1-4 from the following options 1 (check for primality), 2 (generate a prime), 3 (encrypt a message), or 4 (to quit): "))
        print("You chose option", option)
    except ValueError:
        print("Please enter an integer")
        main()
        return
    if 0 < option < 5:
        problemSelector(option)
    else:
        print("Invalid Option, you needed to type a 1, 2, 3, or 4....")
        main()
def problemSelector(option):
    if option == 1:
        problem1()
    elif option == 2:
        problem2()
    elif option == 3:
        problem3()
    elif option == 4:
        exit()
    main()
def problem1():
    N = 0
    K = 0
    while N <= 0:
        N = int(input("Choose an input N to check for primality (must be positive): "))
    while K <= 0:
        K = int(input("Choose K amount of times you want it tested (must be positive): "))
    isPrime = primality3(N, K)
    print(isPrime)
def problem2():
    N = 0
    K = 0
    while N <= 0:
        N = int(input("Choose an input size N to make binary prime number of N bits (must be positive): "))
    while K <= 0:
        K = int(input("Choose K amount of times you want it tested (must be positive): "))
    primeNum = generatePrime(N, K)
    print(primeNum)
    main()
def problem3():
    N = 0
    K = 0
    while N <= 0:
        N = int(input("Choose an input N to make prime number of N bits (must be positive, larger input required for encryption of longer messages): "))
    while K <= 0:
        K = int(input("Choose K amount of times you want it tested for primality (must be positive): "))
    M = input("Choose string or integer M to be encrypted: ")
    try:
        M = int(M)
        stringFlag = 0
    except ValueError:
        M = stringToInt(M)
        stringFlag = 1
    RSA(N, K, M, stringFlag)
if __name__ == "__main__":
    main()