def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
def print_fibonacci_sequence():
    for n in range(47):
        fib_n = fibonacci_recursive(n)
        print(f"{n}\t{fib_n}")
if __name__ == "__main__":
    print_fibonacci_sequence()