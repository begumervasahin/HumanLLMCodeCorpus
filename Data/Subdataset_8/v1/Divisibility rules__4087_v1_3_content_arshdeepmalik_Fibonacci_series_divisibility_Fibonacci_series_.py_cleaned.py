import random
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def fizzbuzz(n):
    fibonacci_s = ""
    if is_prime(n):
        return "BuzzFizz"
    if n % 3 == 0:
        fibonacci_s += "Fizz"
    if n % 5 == 0:
        fibonacci_s += "Buzz"
    if fibonacci_s == "":
        return str(n)
    return fibonacci_s
def is_prime(n):
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    n = 15
    fib_print = []
    fb_print = []
    for f in range(n):
        fib_sum = fibonacci(f)
        fb = fizzbuzz(fib_sum)
        fib_print.append(fib_sum)
        fb_print.append(fb)
    print("Fibonacci - Fizzbuzz:")
    for r in range(n):
        print(fib_print[r], "->", fb_print[r])