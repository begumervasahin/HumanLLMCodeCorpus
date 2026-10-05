def fizzbuzz_program():
    upper_limit = input("Enter the upper limit (numerical value only) for the evaluation:\n")
    try:
        max_value = int(upper_limit) + 1
        for num in range(1, max_value):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz!")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
    except ValueError:
        print("Error: Please enter a valid numerical value.")
if __name__ == "__main__":
    fizzbuzz_program()