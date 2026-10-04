class class1:
    pass
class class2:
    pass
class class3:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        a1 = 0
        a1 += self.fonk3()
        a1 += self.fonk4()
        a1 += self.fonk5()
        a1 += self.fonk6()
        a1 += self.fonk7()
        a1 += self.fonk8()
        return a1
    def fonk3(self):
        return 0
    def fonk4(self):
        return 0
    def fonk5(self):
        return 0
    def fonk6(self):
        return 0
    def fonk7(self):
        return 0
    def fonk8(self):
        return 0
class class4:
    a2 = 1
    a3 = 2
    def fonk9(self, b3):
        self.b3 = b3
        self.b4 = open(b3, 'w')
    def fonk10(self, message, level):
        self.fonk11(message, level)
        print(message)
    def fonk11(self, message, level):
        if level >= self.a2:
            self.b4.write(message + '\n')
    def fonk12(self):
        self.b4.close()
    def fonk13(self, b3):
        self.b4 = open(b3, 'w')
from linkedLists import class5, class6
from linkedListsTests import class3
from testLogger import class4
def fonk14():
    a4 = 0
    b5 = class4("SingleLinkedListTest.txt")
    b5.fonk10("Testing class class5", b5.a2)
    b6 = class3(class5, b5.log)
    a4 += b6.fonk2()
    if a4 = = 0:
        b7 = f"class5 TEST PASSED with {a4} errors"
    else:
        b7 = f"class5 TEST FAILED with {a4} errors"
    b5.fonk10(b7, b5.a3)
    b5.fonk12()
    del b6
    a4 = 0
    b5.fonk13("DoubleLinkedListTest.txt")
    b5.fonk10("Testing class class6", b5.a2)
    b6 = class3(class6, b5.log)
    a4 += b6.fonk3()
    a4 += b6.fonk4()
    a4 += b6.fonk5()
    a4 += b6.fonk6()
    a4 += b6.fonk7()
    a4 += b6.fonk8()
    if a4 = = 0:
        b7 = f"class6 TEST PASSED with {a4} errors"
    else:
        b7 = f"class6 TEST FAILED with {a4} errors"
    b5.fonk10(b7, b5.a3)
    b5.fonk12()
if b8 = = "__main__":
    fonk14()