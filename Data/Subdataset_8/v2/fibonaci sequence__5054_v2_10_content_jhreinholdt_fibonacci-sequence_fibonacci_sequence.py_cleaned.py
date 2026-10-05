
def fibonacci_number(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci_number(position - 2) + fibonacci_number(position - 1)
def fibonacci_sequence(num_elements):
    if num_elements <= 0:
        print("Please enter a positive integer")
    else:
        print("The Fibonacci Sequence with", num_elements, "elements is:")
        for position in range(num_elements):
            print(fibonacci_number(position), "", end="")
def main():
    while True:
        try:
            num_elements = int(input('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: '))
            fibonacci_sequence(num_elements)
            break
        except ValueError:
            print("Please enter a valid positive integer.")
if __name__ == '__main__':
    main()