import time
from threading import Thread, Timer
class class1(Thread):
    def fonk1(self, b2, b1):
        Thread.fonk3(self)
        self.b1 = b1
        self.b2 = b2
        self.b3 = True
        self.b4 = False
    def fonk2(self):
        while not self.b4:
            time.sleep(self.b2)
            self.b1()
class class2(object):
    def fonk3(self, b2, b6, b5 = None):
        if b5:
            assert type(b5) is list
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