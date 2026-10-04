
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
                print("Please enter a positive integer.")
        except ValueError:
            print("Please only input an integer.")
def print_fibonacci_sequence(term):
    print("\nFibonacci sequence:\n")
    for num in range(term + 1):
        print(recursive_fibo(num))
def main():
    term = get_positive_integer('Up to how many terms to return Fibonacci?: ')
    print_fibonacci_sequence(term)
if __name__ == "__main__":
    main()