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
            my_sum = sum(self.previous[:-1])
            self.ratio = my_sum / self.previous[-1]
            self.steps += 1
            if len(self.previous) >= self.padtype:
                new_array = self.previous[slice(len(self.previous) - self.padtype, len(self.previous))]
                new_array.append(my_sum)
                self.previous = new_array
            else:
                self.previous.append(my_sum)
            self.padovan()
if __name__ == "__main__":
    for i in range(2, 77):
        my_pad = Padovan(i, 90)
        my_pad.padovan()