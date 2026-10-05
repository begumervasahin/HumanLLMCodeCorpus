class Fibonacci:
    def __init__(self, fib_type=2, stop=10):
        self.steps = 0
        self.ratio = 0
        self.fib_type = fib_type
        self.stop = stop
        self.previous = [1, 1]
    def calculate_fibonacci(self):
        while self.steps < self.stop:
            my_sum = sum(self.previous)
            self.ratio = my_sum / self.previous[-1]
            self.steps += 1
            if len(self.previous) >= self.fib_type:
                self.previous.pop(0)
            self.previous.append(my_sum)
        print(f"Ratio {self.fib_type}: {self.ratio}")
if __name__ == "__main__":
    for i in range(55):
        my_fib = Fibonacci(i, 54)
        my_fib.calculate_fibonacci()