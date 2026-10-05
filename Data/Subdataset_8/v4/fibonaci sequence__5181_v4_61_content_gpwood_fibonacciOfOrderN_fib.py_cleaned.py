class Fibonacci:
    def __init__(self, fib_type=2, stop=10):
        self.steps = 0
        self.ratio = 0
        self.fib_type = fib_type
        self.stop = stop
        self.previous = [1, 1]
    def calculate_fibonacci(self):
        if self.stop == self.steps:
            print(f"Ratio {self.fib_type}: {self.ratio}")
            return
        else:
            my_sum = sum(self.previous)
            self.ratio = my_sum / self.previous[-1]
            self.steps += 1
            if len(self.previous) >= self.fib_type:
                new_array = self.previous[slice(len(self.previous) + 1 - self.fib_type, len(self.previous))]
                new_array.append(my_sum)
                self.previous = new_array
            else:
                self.previous.append(my_sum)
            self.calculate_fibonacci()
if __name__ == "__main__":
    for i in range(55):
        my_fib = Fibonacci(i, 54)
        my_fib.calculate_fibonacci()