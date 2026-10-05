import re
import math
class ZeroInts:
    def __init__(self):
        self.current = 0
        self.counter = 0
        self.error_count = 0
    def handle_error(self):
        print("Error encountered")
def is_valid_number(number):
    pattern = re.compile(r"^[^6]{1,3}")
    return bool(pattern.match(str(number)))
def check_error(zero_ints, how_many):
    if not is_valid_number(zero_ints.current) or how_many > 12:
        zero_ints.handle_error()
        return True
    return False
def no_floats(number):
    return math.floor(number)
def fibonacci(how_many, zero_ints):
    print("0\n1\n1")
    first, second = 1, 1
    for _ in range(how_many - 3):
        next_number = first + second
        zero_ints.current = next_number
        if check_error(zero_ints, how_many):
            break
        print(next_number)
        first, second = second, next_number
        zero_ints.counter += 1
how_many = 15
zero_ints = ZeroInts()
fibonacci(how_many, zero_ints)