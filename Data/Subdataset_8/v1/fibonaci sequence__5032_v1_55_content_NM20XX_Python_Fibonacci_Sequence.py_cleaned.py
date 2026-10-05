def fib_generator(n):
    x = 0
    y = 1
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
    cnt = 0
    x, y = 0, 1
    while cnt < term:
        if term == 1:
            print(x)
        else:
            print(x, end=', ')
            x, y = y, x + y
        cnt += 1
def main():
    choice = input("Choose an approach (1 - Generator Function, 2 - While Loop): ")
    if choice == "1":
        term = get_input()
        for n in fib_generator(term):
            print(n)
    elif choice == "2":
        generate_fibonacci_sequence()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")
if __name__ == "__main__":
    main()