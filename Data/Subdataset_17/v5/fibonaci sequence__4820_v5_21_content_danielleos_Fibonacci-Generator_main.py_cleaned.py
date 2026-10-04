def generate_fibonacci_sequence(count):
    if count < 1:
        return []
    fib_list = [0, 1]
    while len(fib_list) < count:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list[:count]
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Sorry, the number must be positive. Please try again.")
        except ValueError:
            print("Sorry, I did not understand that input. Please enter a whole number.")
def main():
    count = get_positive_integer("How many Fibonacci numbers do you want to see? ")
    print(f"Producing {count} Fibonacci numbers...")
    fib_sequence = generate_fibonacci_sequence(count)
    print(fib_sequence)
if __name__ == "__main__":
    main()