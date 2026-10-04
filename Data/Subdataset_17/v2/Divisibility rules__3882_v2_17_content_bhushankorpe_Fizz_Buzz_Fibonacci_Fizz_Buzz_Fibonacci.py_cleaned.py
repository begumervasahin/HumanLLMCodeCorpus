def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
def process_number(num):
    results = []
    if num % 3 == 0:
        results.append("Buzz")
    if num % 5 == 0:
        results.append("Fizz")
    if num % 15 == 0:
        results.append("FizzBuzz")
    if is_prime(num):
        results.append("BuzzFizz")
    if results:
        for item in results:
            print(item)
    else:
        fibonacci_sequence = generate_fibonacci(num)
        print(fibonacci_sequence)
def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == '__main__':
    n = int(input("How many Fibonacci numbers do you want to see? "))
    process_number(n)