class Fibonacci:
    def __init__(self, fib_type=2, stop=10):
        self.steps = 0
        self.ratio = 0
        self.fib_type = fib_type
        self.stop = stop
        self.previous_fibs = [1, 1]
    def calculate_fibonacci(self):
        while self.steps < self.stop:
            self.steps += 1
            current_sum = sum(self.previous_fibs)
            self.ratio = current_sum / self.previous_fibs[-1]
            if len(self.previous_fibs) >= self.fib_type:
                self.previous_fibs.pop(0)
            self.previous_fibs.append(current_sum)
        print(f"Ratio {self.fib_type}: {self.ratio}")
if __name__ == "__main__":
    for i in range(55):
        fib_instance = Fibonacci(i, 54)
        fib_instance.calculate_fibonacci()