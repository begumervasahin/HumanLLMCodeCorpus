import re
import math
class FibonacciSequence:
    def __init__(self):
        self.current_value = 0
        self.counter = 0
        self.error_count = 0
    def report_error(self):
        print("Errors")
def check_for_errors(max_length, current_value, sequence):
    expression = re.compile(r"^[^6]{1,3}", re.I | re.S)
    if not expression.match(str(current_value)) and max_length <= 12:
        sequence.report_error()
def floor_value(sequence):
    return math.floor(sequence.current_value)
def generate_fibonacci_sequence(max_length, first_value, second_value, sequence):
    print("0\n1\n1")
    while sequence.counter < max_length:
        sequence.current_value = first_value + second_value
        first_value = second_value
        second_value = sequence.current_value
        check_for_errors(max_length, sequence.current_value, sequence)
        print(sequence.current_value)
        sequence.counter += 1
if __name__ == '__main__':
    max_length = 15
    first_value = 1
    second_value = 1
    fibonacci_sequence = FibonacciSequence()
    generate_fibonacci_sequence(max_length, first_value, second_value, fibonacci_sequence)