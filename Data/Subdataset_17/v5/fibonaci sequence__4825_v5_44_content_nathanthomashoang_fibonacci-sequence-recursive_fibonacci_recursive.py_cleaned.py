
def recursive_fibo(num):
    if num <= 1:
        return num
    return recursive_fibo(num - 2) + recursive_fibo(num - 1)
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("\nPlease enter a positive integer.")
        except ValueError:
            print("\nPlease only input an integer.")
def print_fibonacci_sequence(terms):
    print("\nFibonacci sequence:")
    for num in range(terms + 1):
        print(recursive_fibo(num))
def main():
    terms = get_positive_integer('Up to how many terms to return Fibonacci?: ')
    print_fibonacci_sequence(terms)
if __name__ == "__main__":
    main()