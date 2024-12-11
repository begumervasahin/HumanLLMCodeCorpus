import time
class class1:
    def fonk1(self, b1 = None, b2=False):
        self.b1 = b1
        self.b2 = b2
        self.fonk5()
    @property
    def fonk2(self):
        return self.b3
    def fonk3(self):
        self.b3 = time.time() - self.b4
        return self.finish_time
    def fonk4(self):
        self.b3 = self.fonk3()
        if self.b2:
            print(f"{self.b1} took {self}")
    def fonk5(self):
        self.b3 = None
        self.b4 = time.time()
    def fonk6(self):
        b5 = self.fonk3()
        if b5 < 1:
            return f"{round(1000 * b5)} ms"
        elif b5 < 10:
            return f"{b5:.1f} sec"
        else:
            b6 = round(b5)
            if b6 < 60:
                return f"{b6} sec"
            elif b6 < 3600:
                return f"{b6
            elif b6 < 86400:
                return f"{b6
            else:
                b7 = b6
                b6 %= 86400
                b8 = b6
                b6 %= 3600
                b9 = b6
                b10 = b6 % 60
                return f"{b7}-{b8}:{b9:02d}:{b10:02d} d-h:m:s"
    def fonk7(self):
        self.fonk5()
    def fonk8(self, type, value, traceback):
        self.fonk4()
if b11 = = "__main__":
    b12 = class1("foobar", True)
    time.sleep(0.1)
    b12.fonk4()
    print("Finish time:", b12.finish_time)
    with class1("foobar2", True):
        time.sleep(0.1)