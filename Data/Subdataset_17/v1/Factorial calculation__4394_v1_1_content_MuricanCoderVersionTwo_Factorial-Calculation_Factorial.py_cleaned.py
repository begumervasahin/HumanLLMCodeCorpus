import sys
import datetime
import functools
import operator
import decimal
def factorial(n):
    return functools.reduce(operator.mul, range(1, n + 1), 1)
def log_time_and_result(start_time, end_time, number, result):
    time_difference = (end_time - start_time).total_seconds()
    with open("Factorial.txt", "a") as file:
        file.write(f"Start time: {start_time.strftime('%H%M%S.%f')}\n")
        file.write(f"End time: {end_time.strftime('%H%M%S.%f')}\n")
        file.write(f"Factorial of {number} is {format(result, '.6e')}\n")
        file.write(f"The time difference is {time_difference} seconds\n")
def main():
    max_number = int(input('What will the maximum count be?: '))
    number_increase = int(input('What will be the number added per round?: '))
    number = 0
    while number < max_number:
        number += number_increase
        start_time = datetime.datetime.now()
        result = factorial(number)
        end_time = datetime.datetime.now()
        log_time_and_result(start_time, end_time, number, decimal.Decimal(result))
if __name__ == "__main__":
    main()