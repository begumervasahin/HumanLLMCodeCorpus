def generate_fibonacci_sequence(count):
    if count < 1:
        return []
    fib_list = [0]
    if count > 1:
        fib_list.append(1)
    for _ in range(2, count):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Sorry, seems like that is not a positive integer, try again please.")
        except ValueError:
            print("Sorry, I did not understand that input, please input a whole number.")
def main():
    count = get_positive_integer("How many Fibonacci numbers do you want to see? ")
    print(f"Producing {count} Fibonacci numbers...")
    fib_sequence = generate_fibonacci_sequence(count)
    print(fib_sequence)
if __name__ == "__main__":
    main()