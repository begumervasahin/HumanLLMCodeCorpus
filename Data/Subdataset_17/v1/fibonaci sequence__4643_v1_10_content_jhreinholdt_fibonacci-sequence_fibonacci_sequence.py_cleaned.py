
def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 2) + fibonacci_number(n - 1)
def fibonacci_sequence(num_elements):
    if num_elements <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"The Fibonacci Sequence with {num_elements} elements is:")
        for k in range(num_elements):
            print(fibonacci_number(k), end=" ")
        print()
def main():
    while True:
        try:
            num_elements = int(input('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: '))
            fibonacci_sequence(num_elements)
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
if __name__ == '__main__':
    main()