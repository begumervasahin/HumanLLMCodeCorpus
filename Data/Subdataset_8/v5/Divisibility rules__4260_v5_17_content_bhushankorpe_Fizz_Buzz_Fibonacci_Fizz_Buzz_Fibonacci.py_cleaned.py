def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence
def print_output(num):
    if num % 3 == 0:
        print("Buzz")
    if num % 5 == 0:
        print("Fizz")
    if num % 15 == 0:
        print("FizzBuzz")
    if is_prime(num):
        print("BuzzFizz")
    else:
        fibonacci_sequence = generate_fibonacci_sequence(num)
        print(fibonacci_sequence)
if __name__ == '__main__':
    print("How many Fibonacci numbers do you want to see?")
    n = int(input())
    print_output(n)