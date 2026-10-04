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
        self.b4 = self.fonk3()
        if self.b3:
            print(f"{self.b2} took {self}")
    def fonk5(self):
        self.b4 = None
        self.b5 = time.time()
    def fonk6(self):
        b6 = self.fonk3()
        if b6 < 1:
            return f"{round(1000 * b6)} ms"
        elif b6 < 10:
            return f"{b6:.1f} sec"
        else:
            b7 = round(b6)
            if b7 < 60:
                return f"{b7} sec"
            elif b7 < 3600:
                return f"{b7
            elif b7 < 86400:
                return f"{b7
            else:
                return f"{b7
    def fonk7(self):
        self.fonk5()
        return self
    def fonk8(self, exc_type, exc_value, traceback):
        self.fonk4()
if b8 = = "__main__":
    b9 = class1("foobar", True)
    time.sleep(0.1)
    b9.fonk4()
    print(f"Elapsed time: {b9.finishtime} seconds")
    with class1("foobar2", True):
        time.sleep(0.1)