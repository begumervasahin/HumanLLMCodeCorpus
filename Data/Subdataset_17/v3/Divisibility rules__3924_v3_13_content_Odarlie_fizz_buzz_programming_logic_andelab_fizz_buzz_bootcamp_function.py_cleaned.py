def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number
def print_fizz_buzz(start, end):
    for i in range(start, end + 1):
        print(fizz_buzz(i))
def main():
    print_fizz_buzz(1, 100)
if __name__ == "__main__":
    main()