
def recursive_fibo(num):
    if num <= 1:
        return num
    return recursive_fibo(num - 2) + recursive_fibo(num - 1)
def shell():
    while True:
        try:
            term = int(input('Up to how many terms to return Fibonacci?: '))
            if term <= 0:
                print("\nPlease enter a positive integer")
            else:
                break
        except ValueError:
            print('\nPlease only input an integer.')
    print("\nFibonacci sequence:\n")
    for num in range(term + 1):
        print(recursive_fibo(num))
if __name__ == "__main__":
    shell()