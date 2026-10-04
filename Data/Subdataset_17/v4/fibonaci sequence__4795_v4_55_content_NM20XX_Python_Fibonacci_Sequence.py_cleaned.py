def fib(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y
def get_input():
    while True:
        try:
            term = int(input("Enter a term in the Fibonacci sequence: "))
            if term <= 0:
                print("Enter a positive integer value.")
            else:
                return term
        except ValueError:
            print("Error: Please enter a valid integer value.")
def main():
    input_term = get_input()
    print(f"Fibonacci sequence up to {input_term} terms:")
    for number in fib(input_term):
        print(number, end=', ')
    print()
if __name__ == "__main__":
    main()
