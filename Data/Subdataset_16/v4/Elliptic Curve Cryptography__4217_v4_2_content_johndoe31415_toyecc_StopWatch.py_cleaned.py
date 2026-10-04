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
            return f"{round(1000 * b6)} ms"
        elif b6 < 10:
            return f"{b6:.1f} sec"
        else:
            b7 = round(b6)
            if b7 < 60:
                return f"{b7} sec"
            elif b7 < 3600:
                minutes, b8 = divmod(b7, 60)
                return f"{minutes}:{b8:02d} m:s"
            elif b7 < 86400:
                hours, b9 = divmod(b7, 3600)
                minutes, b8 = divmod(b9, 60)
                return f"{hours}:{minutes:02d}:{b8:02d} h:m:s"
            else:
                days, b9 = divmod(b7, 86400)
                hours, b9 = divmod(b9, 3600)
                minutes, b8 = divmod(b9, 60)
                return f"{days}-{hours}:{minutes:02d}:{b8:02d} d-h:m:s"
    def fonk7(self):
        self.fonk5()
        return self
    def fonk8(self, exc_type, exc_value, traceback):
        self.fonk4()
if b10 = = "__main__":
    b11 = class1("foobar", True)
    time.sleep(0.1)
    b11.fonk4()
    print(f"Elapsed time: {b11.finishtime} b8")
    with class1("foobar2", True):
        time.sleep(0.1)