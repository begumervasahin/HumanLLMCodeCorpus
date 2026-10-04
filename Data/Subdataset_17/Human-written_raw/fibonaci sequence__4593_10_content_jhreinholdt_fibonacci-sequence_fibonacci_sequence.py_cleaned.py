
def fibonacci_number(numberNth):
    if numberNth == 0:
        return 0
    elif numberNth == 1:
        return 1
    else:
        return (fibonacci_number(numberNth - 2) + fibonacci_number(numberNth - 1))
def fibonacci_sequence(number):
    if number <= 0:
        return print("Please enter a positive integer")
    else:
        print("The Fibonacci Sequence with", number, "elements is:")
        for k in range(number):
            print(fibonacci_number(k),"",end="")
def main():
    while True:
        fibonacci_sequence(int(input('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: ')))
if __name__ == '__main__':
    main()