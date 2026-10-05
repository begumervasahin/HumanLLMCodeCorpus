def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
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
        fibo_sequence = fibonacci_sequence(num)
        print(fibo_sequence)
if __name__ == '__main__':
    print("How many Fibonacci numbers do you want to see?")
    n = int(input())
    print_output(n)