class Padovan:
    def __init__(self, padtype=2, stop=10):
        self.steps = 0
        self.ratio = 0
        self.padtype = padtype
        self.stop = stop
        self.previous = [1, 1, 1]
    def calculate(self):
        if self.steps == self.stop:
            print(f"Ratio {self.padtype}: {self.ratio:.5f}")
            return
        current_sum = sum(self.previous[:-1])
        self.ratio = current_sum / self.previous[-1]
        self.steps += 1
        if len(self.previous) >= self.padtype:
            self.previous = self.previous[-self.padtype + 1:] + [current_sum]
        else:
            self.previous.append(current_sum)
        self.calculate()
def main():
    for padtype in range(2, 77):
        padovan = Padovan(padtype, 90)
        padovan.calculate()
if __name__ == "__main__":
    main()