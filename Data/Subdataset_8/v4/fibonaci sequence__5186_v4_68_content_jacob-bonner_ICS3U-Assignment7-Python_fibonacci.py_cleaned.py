def generate_fibonacci_list():
    fibonacci_list = [1, 1]
    for _ in range(98):
        next_fib = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fib)
    return fibonacci_list
def print_fibonacci_sequence(fibonacci_list):
    for i, fib_num in enumerate(fibonacci_list):
        if i == 0:
            print(f"{fib_num} + 0 = {fib_num}")
        elif i == 1:
            print(f"0 + {fib_num} = {fib_num}")
        else:
            prev_fib = fibonacci_list[i - 1]
            prev_prev_fib = fibonacci_list[i - 2]
            print(f"{prev_prev_fib} + {prev_fib} = {fib_num}")
def main():
    fibonacci_list = generate_fibonacci_list()
    print_fibonacci_sequence(fibonacci_list)
if __name__ == "__main__":
    main()