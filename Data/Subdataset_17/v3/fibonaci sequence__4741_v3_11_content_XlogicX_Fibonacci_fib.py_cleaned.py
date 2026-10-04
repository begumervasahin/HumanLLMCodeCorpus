import re
import math
class FibonacciSequence:
    def __init__(self):
        self.current = 0
        self.count = 0
        self.error_count = 0
    def report_error(self):
        print("Errors")
def check_for_errors(sequence_length, current_value, error_count, sequence):
    expression = re.compile(r"^[^6]{1,3}", re.I | re.S)
    if not expression.match(str(current_value)):
        if sequence_length > 12:
            return
        sequence.report_error()
def floor_value(sequence):
    return math.floor(sequence.current)
def generate_fibonacci(sequence_length, first_value, second_value, sequence):
    print("0\n1\n1")
    while sequence.count < sequence_length:
        sequence.current = first_value + second_value
        first_value = second_value
        second_value = sequence.current
        check_for_errors(sequence_length, sequence.current, sequence.error_count, sequence)
        print(sequence.current)
        sequence.count += 1
if __name__ == '__main__':
    sequence_length = 15
    first_value = 1
    second_value = 1
    fibonacci_sequence = FibonacciSequence()
    generate_fibonacci(sequence_length, first_value, second_value, fibonacci_sequence)