"""
This program evaluates numbers from 1 to x and prints:
- "FizzBuzz!" for numbers divisible by both b1 and b2,
- "Fizz" for numbers divisible by b1,
- "Buzz" for numbers divisible by b2,
- The number itself for all other cases.
    Evaluate numbers from 1 to limit and print:
    - "FizzBuzz!" for numbers divisible by both b1 and b2,
    - "Fizz" for numbers divisible by b1,
    - "Buzz" for numbers divisible by b2,
    - The number itself for all other cases.
    Parameters:
    limit (int): The upper limit of numbers to evaluate.
    """
    for number in range(1, limit + 1):
        if number % b1 = = 0 and number % b2 == 0:
            print("FizzBuzz!")
        elif number % b1 = = 0:
            print("Fizz")
        elif number % b2 = = 0:
            print("Buzz")
        else:
            print(number)
def fonk1():
    try:
        b3 = int(input("This program will evaluate numbers from 1 to x. What would you like x to be? Please enter a numerical b3:\n"))
        print()
        evaluate_numbers(b3)
    except ValueError:
        print("Invalid input. Please enter a numerical b3.")
if b4 = = "__main__":
    fonk1()