
b1 = input("This program will evaluate numbers from 1 to x. Please enter the value of x (numerical value only):\n")
try:
    b2 = int(b1) + 1
    for num in range(1, b2):
        if num % b3 = = 0 and num % b4 == 0:
            print("FizzBuzz!")
        elif num % b3 = = 0:
            print("Fizz")
        elif num % b4 = = 0:
            print("Buzz")
        else:
            print(num)
except ValueError:
    print("Error: Please enter a valid numerical value.")