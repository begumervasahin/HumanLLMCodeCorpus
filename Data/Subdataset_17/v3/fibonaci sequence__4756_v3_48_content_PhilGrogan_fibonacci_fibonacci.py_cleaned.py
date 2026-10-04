
def calculate_fibonacci(n):
    current, previous = 1, 1
    for _ in range(n - 1):
        current, previous = current + previous, current
    return current
def get_ordinal_suffix(number):
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
        position = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
        if position <= 0:
            raise ValueError("The number must be a positive integer.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    fibonacci_number = calculate_fibonacci(position)
    suffix = get_ordinal_suffix(position)
    print(f"{fibonacci_number:,d} is the {position:,d}{suffix} number of the Fibonacci sequence.")
if __name__ == "__main__":
    main()