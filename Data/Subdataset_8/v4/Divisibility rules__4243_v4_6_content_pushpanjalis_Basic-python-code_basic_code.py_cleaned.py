
def check_divisibility(number):
    if number % 2 == 0:
        print('The number is divisible by 2')
    elif number % 3 == 0:
        print('The number is divisible by 3')
    elif number % 5 == 0:
        print('The number is divisible by 5')
    elif number % 7 == 0:
        print('The number is divisible by 7')
    else:
        print('The number is not divisible by 2, 3, 5, or 7')
number = int(input('Select a number of your choice:\n'))
check_divisibility(number)