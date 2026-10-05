class Counter:
    def __init__(self, count, initial_value=0, zeros=True):
        self.count = count
        self.digits = []
        self.overflow = False
        if initial_value != 0:
            self._initialize_from_value(initial_value)
        else:
            self._initialize_with_zeros(zeros)
    def _initialize_from_value(self, initial_value):
        self.digits = [int(digit) for digit in str(initial_value)]
        self._pad_with_zeros()
    def _initialize_with_zeros(self, zeros):
        self.digits = [0 if zeros else 1] * self.count
    def _pad_with_zeros(self):
        while len(self.digits) < self.count:
            self.digits.insert(0, 0)
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