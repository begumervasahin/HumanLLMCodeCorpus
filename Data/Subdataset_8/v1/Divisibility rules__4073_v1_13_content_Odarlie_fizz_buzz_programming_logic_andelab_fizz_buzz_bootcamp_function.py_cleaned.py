def fizz_buzz(number):
    '''
    This function returns 'Fizz,'Buzz,FizzBuzz' or the argument it receives based
    on the argument the function receives.
    '''
    if number % 5 == 0 and number % 3 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number
if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = fizz_buzz(num)
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")