import sys
import datetime
import operator
import functools
import decimal
def get_current_time():
    return datetime.datetime.now()
def write_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
def calculate_factorial(max_number, number_increase, filename):
    number1 = 0
    while number1 < max_number:
        number2 = number1 + 1
        number1 += number_increase
        start_time = get_current_time()
        write_to_file(filename, f"Start time {start_time.strftime('%H%m%S.%f')}\n")
        multipliers = [i for i in range(number1, 0, -1)]
        result = functools.reduce(operator.mul, multipliers, 1)
        end_time = get_current_time()
        write_to_file(filename, f"End time {end_time.strftime('%H%m%S.%f')}\n")
        factorial_result = decimal.Decimal(result)
        write_to_file(filename, f"Factorial of {number1} is {format(factorial_result, '.6e')}\n")
        write_to_file(filename, f"The time difference is {(end_time - start_time).total_seconds()} seconds\n")
if __name__ == "__main__":
    max_number = int(input('What will the maximum count be?: '))
    number_increase = int(input('What will be the number added per round?: '))
    calculate_factorial(max_number, number_increase, "Factorial.txt")