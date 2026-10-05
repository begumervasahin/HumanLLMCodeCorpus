def fib_generator(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y
def generate_fibonacci_sequence():
    while True:
        try:
            term = int(input("Enter the term in the Fibonacci sequence: "))
            if term <= 0:
                print("Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    print("Fibonacci sequence up to term", term, ":")
    x, y = 0, 1
    for _ in range(term):
        print(x, end=', ' if term > 1 else '\n')
        x, y = y, x + y
def main():
    print("Choose an approach:")
    print("1 - Generator Function")
    print("2 - While Loop")
    choice = input("Enter your choice: ")
    if choice == "1":
        term = int(input("Enter the term in the Fibonacci sequence: "))
        print("Fibonacci sequence up to term", term, ":")
        for n in fib_generator(term):
            print(n)
    elif choice == "2":
        generate_fibonacci_sequence()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")
if __name__ == "__main__":
    main()