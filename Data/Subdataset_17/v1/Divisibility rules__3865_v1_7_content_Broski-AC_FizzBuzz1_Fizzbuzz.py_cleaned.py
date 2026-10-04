"""
This program evaluates numbers from 1 to x and prints:
- "FizzBuzz!" for numbers divisible by both 3 and 5,
- "Fizz" for numbers divisible by 3,
- "Buzz" for numbers divisible by 5,
- The number itself for all other cases.
"""
def main():
    try:
        value = int(input("This program will evaluate numbers from 1 to x. What would you like x to be? Please only enter a numerical value.\n"))
        print("\n")
        for x in range(1, value + 1):
            if x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz!")
            elif x % 3 == 0:
                print("Fizz")
            elif x % 5 == 0:
                print("Buzz")
            else:
                print(x)
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
if __name__ == "__main__":
    main()