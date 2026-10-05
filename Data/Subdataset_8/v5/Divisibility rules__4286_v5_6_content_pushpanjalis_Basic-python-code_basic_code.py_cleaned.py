def check_divisibility(number):
    if number % 2 == 0:
        print(f'The number {number} is divisible by 2.')
    elif number % 3 == 0:
        print(f'The number {number} is divisible by 3.')
    elif number % 5 == 0:
        print(f'The number {number} is divisible by 5.')
    elif number % 7 == 0:
        print(f'The number {number} is divisible by 7.')
    else:
        print(f'The number {number} is not divisible by 2, 3, 5, or 7.')
def get_user_input():
    while True:
        try:
            number = int(input('Select a number of your choice:\n'))
            return number
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
def main():
    number = get_user_input()
    check_divisibility(number)
if __name__ == '__main__':
    main()