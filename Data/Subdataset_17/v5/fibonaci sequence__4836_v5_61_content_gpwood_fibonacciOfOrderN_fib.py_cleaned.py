class Fibonacci:
    def __init__(self, fibtype=2, stop=10):
        self.steps = 0
        self.ratio = 0
        self.fibtype = fibtype
        self.stop = stop
        self.previous = [1] * fibtype
    def calculate(self):
        if self.steps == self.stop:
            print(f"Ratio {self.fibtype}: {self.ratio}")
            return
        current_sum = sum(self.previous)
        self.ratio = current_sum / self.previous[-1]
        self.steps += 1
        if len(self.previous) >= self.fibtype:
            self.previous = self.previous[1:] + [current_sum]
        else:
            self.previous.append(current_sum)
        self.calculate()
def main():
    for fibtype in range(2, 57):
        fibonacci = Fibonacci(fibtype, 54)
        fibonacci.calculate()
if __name__ == "__main__":
    main()