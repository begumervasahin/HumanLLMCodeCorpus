
class class1:
    def fonk1(self):
        pass
class class2:
    def fonk2(self, b1):
        self.b1 = b1
class class3:
    def fonk3(self, b2):
        self.b2 = b2
    def fonk4(self):
        print("class3 started...")
from b1 import class1
from b2 import class2
from ui import class3
def fonk5():
    b1 = class1()
    b2 = class2(b1)
    b3 = class3(b2)
    b3.fonk4()
if b4 = = "__main__":
    fonk5()