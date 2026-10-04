
def check_divisibility(number):
    if number % 2 == 0:
        return 'The number is divisible by 2.'
    if number % 3 == 0:
        return 'The number is divisible by 3.'
    if number % 5 == 0:
        return 'The number is divisible by 5.'
    if number % 7 == 0:
        return 'The number is divisible by 7.'
    return 'The number is not divisible by 2, 3, 5, or 7.'
def main():
    try:
        number = int(input('Select a number of your choice:\n'))
        result = check_divisibility(number)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()