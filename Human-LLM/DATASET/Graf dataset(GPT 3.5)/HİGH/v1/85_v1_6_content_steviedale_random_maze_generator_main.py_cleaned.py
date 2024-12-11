from b5 import class1
from graphics import class2, RED, GREEN
from time import sleep
a1 = 20
a2 = 25
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        pass
class class2:
    def fonk3(self, b2, b3, b1):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
    def fonk4(self, trace_function):
        pass
b4 = class2(b2=a1, b3=a1, b1=a2)
b5 = class1(a1)
b4.fonk4(b5.complete_trace)