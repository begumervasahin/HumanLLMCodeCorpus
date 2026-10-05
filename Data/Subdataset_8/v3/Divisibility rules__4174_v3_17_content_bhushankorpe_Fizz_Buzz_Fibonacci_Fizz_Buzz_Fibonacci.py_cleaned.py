def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
def perform_operations(num):
    if num % 3 == 0:
        print("Buzz")
    if num % 5 == 0:
        print("Fizz")
    if num % 15 == 0:
        print("FizzBuzz")
    if is_prime(num):
        print("BuzzFizz")
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, num):
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        print(fibonacci_sequence[:num])
if __name__ == '__main__':
    print("How many Fibonacci numbers do you want to see?")
    n = int(input())
    perform_operations(n)