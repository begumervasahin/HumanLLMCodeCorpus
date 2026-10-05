import re
class FibonacciGenerator:
    def __init__(self):
        self.current = 0
        self.next = 1
        self.index = 0
    def print_error(self):
        print("Error encountered")
    def check_for_errors(self, number):
        pattern = re.compile(r"^[^6]{1,3}", re.I | re.S)
        if not pattern.match(str(number)):
            self.print_error()
    def generate_fibonacci(self, limit):
        print("0\n1")
        for _ in range(2, limit + 1):
            self.current, self.next = self.next, self.current + self.next
            self.check_for_errors(self.current)
            print(self.current)
def main():
    limit = 15
    fibonacci_generator = FibonacciGenerator()
    fibonacci_generator.generate_fibonacci(limit)
if __name__ == "__main__":
    main()