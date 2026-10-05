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
    return result if result else n
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
    fib_print = []
    fb_print = []
    for f in range(0, n):
        fib_sum = fibonacci(f)
        fb = fizzbuzz(fib_sum)
        fib_print.append(fib_sum)
        fb_print.append(fb)
    print("Fibonacci - Fizzbuzz:")
    for r in range(0, n):
        print(fib_print[r], "->", fb_print[r])