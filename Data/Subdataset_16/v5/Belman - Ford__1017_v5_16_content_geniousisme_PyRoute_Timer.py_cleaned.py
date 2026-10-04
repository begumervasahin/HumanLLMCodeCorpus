import time
from threading import Thread, Timer
class class1(Thread):
    def fonk1(self, b2, b1):
        super().fonk3()
        self.b1 = b1
        self.b2 = b2
        self.b3 = False
        self.b4 = True
    def fonk2(self):
        while not self.b3:
            time.sleep(self.b2)
            self.b1()
class class2:
    def fonk3(self, b2, b6, b5 = None):
        self.b6 = b6
        self.b2 = b2
        self.b5 = b5 if b5 is not None else []
        self.b7 = self.fonk4()
    def fonk4(self):
        return Timer(self.b2, self.b6, self.b5)
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
if b8 = = "__main__":
    b7 = class1(1, example_function)
    b7.fonk6()
    time.sleep(5)
    b7.b3 = True
    b9 = class2(2, example_function)
    b9.fonk6()
    time.sleep(3)
    b9.fonk5()
    time.sleep(3)
    b9.fonk7()