class Counter:
    def __init__(self, count, initial_value=0, zeros=True):
        self.count = count
        self.digits = []
        self.overflow = False
        if initial_value != 0:
            self.digits = [int(digit) for digit in str(initial_value)]
            while len(self.digits) < count:
                self.digits.insert(0, 0)
        else:
            self.digits = [0 if zeros else 1] * count
    def increment(self):
        self.digits[-1] += 1
        for i in range(self.count - 1, -1, -1):
            if self.digits[i] > 9:
                if i == 0:
                    self.overflow = True
                self.digits[i] = 0
                if i - 1 >= 0:
                    self.digits[i - 1] += 1
    def get_value(self):
        return int(''.join(map(str, self.digits)))
    def get_list(self):
        return self.digits
if __name__ == "__main__":
    counter = Counter(3)
    for _ in range(10):
        counter.increment()
        print("Current value:", counter.get_value())