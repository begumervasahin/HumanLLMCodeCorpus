
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
from class1 import class1
from class2 import class2
from class3 import class3
def fonk5():
    b3 = class1()
    b4 = class2(b3)
    b5 = class3(b4)
    b5.fonk4()
if b6 = = "__main__":
    fonk5()