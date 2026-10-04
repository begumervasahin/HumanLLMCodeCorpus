
def check_divisibility(number):
    if number % 2 == 0:
        return 'The number is divisible by 2.'
    elif number % 3 == 0:
        return 'The number is divisible by 3.'
    elif number % 5 == 0:
        return 'The number is divisible by 5.'
    elif number % 7 == 0:
        return 'The number is divisible by 7.'
    else:
        return 'The number is not divisible by 2, 3, 5, or 7.'
if __name__ == "__main__":
    try:
        number = int(input('Select a number of your choice:\n'))
        result = check_divisibility(number)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")