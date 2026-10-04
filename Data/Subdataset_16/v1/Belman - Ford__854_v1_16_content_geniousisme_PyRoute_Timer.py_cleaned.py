import time
from threading import Thread, Timer
class class1(Thread):
    def fonk1(self, b2, b1):
        super().fonk3()
        self.b1 = b1
        self.b2 = b2
        self.b3 = True
        self.b4 = False
    def fonk2(self):
        while not self.b4:
            time.sleep(self.b2)
            self.b1()
class class2:
    def fonk3(self, b2, b6, b5 = None):
        if b5:
            assert isinstance(b5, list)
        self.b6 = b6
        self.b2 = b2
        self.b5 = b5
        self.b7 = self.fonk4()
    def fonk4(self):
        b8 = Timer(self.b2, self.b6, self.b5)
        b8.b3 = True
        return b8
    def fonk5(self):
        self.fonk7()
        self.b7 = self.fonk4()
        self.fonk6()
    def fonk6(self):
        self.b7.fonk6()
    def fonk7(self):
        self.b7.cancel()
def fonk8():
    print("Function called!")
if b9 = = "__main__":
    b7 = class1(1, example_function)
    b7.fonk6()
    time.sleep(5)
    b7.b4 = True
    b10 = class2(2, example_function)
    b10.fonk6()
    time.sleep(3)
    b10.fonk5()
    time.sleep(3)
    b10.fonk7()