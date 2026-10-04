def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def fizzbuzz(n):
    if is_prime(n):
        return "BuzzFizz"
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result if result else str(n)
def main():
    n = 15
    fibonacci_numbers = [fibonacci(i) for i in range(n)]
    fizzbuzz_results = [fizzbuzz(num) for num in fibonacci_numbers]
    print("Fibonacci - FizzBuzz:")
    for fib_num, fb_result in zip(fibonacci_numbers, fizzbuzz_results):
        print(f"{fib_num} -> {fb_result}")
if __name__ == "__main__":
    main()