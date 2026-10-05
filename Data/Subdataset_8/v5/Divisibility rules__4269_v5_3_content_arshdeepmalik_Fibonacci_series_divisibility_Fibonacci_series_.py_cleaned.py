import random
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def fizzbuzz(n):
    result = ""
    if is_prime(n):
        return "BuzzFizz"
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result if result else str(n)
def is_prime(n):
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    n = 15
    fibonacci_numbers = []
    fizzbuzz_results = []
    for f in range(n):
        fib_number = fibonacci(f)
        fizzbuzz_result = fizzbuzz(fib_number)
        fibonacci_numbers.append(fib_number)
        fizzbuzz_results.append(fizzbuzz_result)
    print("Fibonacci - Fizzbuzz:")
    for r in range(n):
        print(fibonacci_numbers[r], "->", fizzbuzz_results[r])