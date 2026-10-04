
def fibonacci(n):
    current_number = 1
    previous_number = 1
    total = 0
    for _ in range(n - 1):
        total = current_number + previous_number
        previous_number = current_number
        current_number = total
    return current_number
def get_suffix(number):
    if 11 <= number % 100 <= 13:
        return 'th'
    else:
        last_digit = number % 10
        if last_digit == 1:
            return 'st'
        elif last_digit == 2:
            return 'nd'
        elif last_digit == 3:
            return 'rd'
        else:
            return 'th'
def main():
    try:
        i = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
        if i <= 0:
            raise ValueError("The number must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    fib_number = fibonacci(i)
    suffix = get_suffix(i)
    print(f"{fib_number:,d} is the {i:,d}{suffix} number of the Fibonacci sequence.")
if __name__ == "__main__":
    main()