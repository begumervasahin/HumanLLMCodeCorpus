def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)
def fibonacci_sequence(length):
    if length <= 0:
        print("Please enter a positive integer.")
    else:
        print("The Fibonacci sequence with", length, "elements is:")
        for i in range(length):
            print(fibonacci_number(i), end=" ")
def main():
    while True:
        try:
            length = int(input('\nEnter a positive number to generate the Fibonacci sequence with that number of elements: '))
            fibonacci_sequence(length)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
if __name__ == '__main__':
    main()