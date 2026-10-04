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
        mysum = sum(self.previous)
        self.ratio = mysum / self.previous[-1]
        self.steps += 1
        if len(self.previous) >= self.fibtype:
            self.previous = self.previous[1:] + [mysum]
        else:
            self.previous.append(mysum)
        self.calculate()
def main():
    print("Fibonacci Ratios (Ctrl-C to Exit):")
    try:
        for i in range(2, 56):
            fib = Fibonacci(i, 54)
            fib.calculate()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
if __name__ == "__main__":
    main()