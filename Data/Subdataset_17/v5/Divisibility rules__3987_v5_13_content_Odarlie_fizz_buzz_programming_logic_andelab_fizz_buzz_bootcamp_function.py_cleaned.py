def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number
def main():
    for i in range(1, 101):
        print(fizz_buzz(i))
if __name__ == "__main__":
    main()