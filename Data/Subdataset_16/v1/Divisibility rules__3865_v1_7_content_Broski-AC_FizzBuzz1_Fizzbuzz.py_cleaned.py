"""
This program evaluates numbers from 1 to x and prints:
- "FizzBuzz!" for numbers divisible by both b2 and b3,
- "Fizz" for numbers divisible by b2,
- "Buzz" for numbers divisible by b3,
- The number itself for all other cases.
"""
def fonk1():
    try:
        b1 = int(input("This program will evaluate numbers from 1 to x. What would you like x to be? Please only enter a numerical b1.\n"))
        print("\n")
        for x in range(1, b1 + 1):
            if x % b2 = = 0 and x % b3 == 0:
                print("FizzBuzz!")
            elif x % b2 = = 0:
                print("Fizz")
            elif x % b3 = = 0:
                print("Buzz")
            else:
                print(x)
    except ValueError:
        print("Invalid input. Please enter a numerical b1.")
if b4 = = "__main__":
    fonk1()