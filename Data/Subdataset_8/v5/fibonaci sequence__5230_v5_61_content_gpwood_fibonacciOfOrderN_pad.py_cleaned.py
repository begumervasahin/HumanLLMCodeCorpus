class Padovan:
    def __init__(self, padtype=2, stop=10):
        self.steps = 0
        self.ratio = 0
        self.padtype = padtype
        self.stop = stop
        self.previous = [1, 1, 1]
    def padovan(self):
        if self.stop == self.steps:
            print(f"Ratio {self.padtype}: {self.ratio}")
            return
        else:
            current_sum = sum(self.previous[:-1])
            self.ratio = current_sum / self.previous[-1]
            self.steps += 1
            if len(self.previous) >= self.padtype:
                new_array = self.previous[-self.padtype:] + [current_sum]
                self.previous = new_array
            else:
                self.previous.append(current_sum)
            self.padovan()
def generate_padovan_sequence():
    for i in range(2, 77):
        padovan_instance = Padovan(i, 90)
        padovan_instance.padovan()
if __name__ == "__main__":
    generate_padovan_sequence()