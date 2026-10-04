class Counter:
    def __init__(self, count, initial_value=0, zeros=True):
        self.count = count
        self.digits = []
        self.overflow = False
        if initial_value != 0:
            self.digits = [int(digit) for digit in str(initial_value)]
            self.digits.reverse()
            while len(self.digits) < count:
                self.digits.append(0)
            self.digits.reverse()
        else:
            self.digits = [0 if zeros else 1 for _ in range(count)]
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
    counter = Counter(5, initial_value=123)
    print("Initial value:", counter.get_value())
    print("Initial list:", counter.get_list())
    counter.increment()
    print("After incrementing:", counter.get_value())
    print("After incrementing list:", counter.get_list())
    for _ in range(10):
        counter.increment()
        print("Value:", counter.get_value())
        print("List:", counter.get_list())
    counter = Counter(3, initial_value=999)
    counter.increment()
    print("Overflow value:", counter.get_value())
    print("Overflow flag:", counter.overflow)
