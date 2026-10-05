import cProfile
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def compute_and_print_fibonacci_numbers(limit):
    for n in range(1, limit + 1):
        result = fibonacci(n)
        print(f"{n}\t{result}")
if __name__ == "__main__":
    cProfile.run("compute_and_print_fibonacci_numbers(47)", filename="profile_results.txt")