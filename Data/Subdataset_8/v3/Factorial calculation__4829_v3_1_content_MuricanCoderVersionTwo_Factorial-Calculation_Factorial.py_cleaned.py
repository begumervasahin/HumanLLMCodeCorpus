import sys
import datetime
import operator
import functools
import decimal
def calculate_factorial(max_number, number_increase):
    number1 = 0
    while number1 < max_number:
        number1 += number_increase
        multipliers = list(range(number1, 0, -1))
        start_time = datetime.datetime.now()
        write_time_to_file("Start time", start_time)
        result = functools.reduce(operator.mul, multipliers, 1)
        end_time = datetime.datetime.now()
        write_time_to_file("End time", end_time)
        write_to_file(f"Factorial of {number1} is {format(decimal.Decimal(result), '.6e')}")
        write_to_file(f"The time difference is {(end_time - start_time).total_seconds()} seconds")
def write_time_to_file(message, time):
    with open("Factorial.txt", "a") as file:
        file.write(f"{message} {time.strftime('%H%m%S.%f')}\n")
def write_to_file(message):
    with open("Factorial.txt", "a") as file:
        file.write(f"{message}\n")
if __name__ == "__main__":
    max_number = int(input('What will the maximum count be?: '))
    number_increase = int(input('What will be the number added per round?: '))
    calculate_factorial(max_number, number_increase)