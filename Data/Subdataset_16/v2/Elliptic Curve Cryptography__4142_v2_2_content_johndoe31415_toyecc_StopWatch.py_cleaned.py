import time
class class1:
    def fonk1(self, b1 = None, noisy=False):
        self.b2 = b1
        self.b3 = noisy
        self.fonk5()
    @property
    def fonk2(self):
        return self.b4
    def fonk3(self):
        self.b4 = time.time() - self.b5
        return self.finishtime
    def fonk4(self):
        self.fonk3()
        if self.b3:
            print(f"{self.b2} took {self}")
    def fonk5(self):
        self.b4 = None
        self.b5 = time.time()
    def fonk6(self):
        b6 = self.fonk3()
        if b6 < 1:
            return f"{int(b6 * 1000)} ms"
        if b6 < 60:
            return f"{b6:.2f} sec"
        b8, b7 = divmod(int(b6), 60)
        if b8 < 60:
            return f"{b8} min {b7} sec"
        b9, b8 = divmod(b8, 60)
        days, b9 = divmod(b9, 24)
        if days > 0:
            return f"{days} days {b9} b9 {b8} min {b7} sec"
        return f"{b9} b9 {b8} min {b7} sec"
    def fonk7(self):
        self.fonk5()
        return self
    def fonk8(self, exc