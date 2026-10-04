import re
import math
class ZeroInts:
    def __init__(self):
        self.current_value = 0
        self.counter = 0
        self.error_count = 0
    def report_error(self):
        print("Errors")
def check_for_errors(hwmny, current_value, error_count):
    expression = re.compile(r"^[^6]{1,3}", re.I | re.S)
    if not expression.match(str(current_value)):
        if hwmny > 12:
            return
        zints.report_error()
def floor_value():
    return math.floor(zints.current_value)
def generate_fibonacci(hwmny, int1, int2):
    print("0\n1\n1")
    while zints.counter < hwmny:
        zints.current_value = int1 + int2
        int1 = int2
        int2 = zints.current_value
        check_for_errors(hwmny, zints.current_value, zints.error_count)
        print(zints.current_value)
        zints.counter += 1
if __name__ == '__main__':
    hwmny = 15
    int1 = 1
    int2 = 1
    zints = ZeroInts()
    generate_fibonacci(hwmny, int1, int2)