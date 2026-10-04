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
        self.b2("Running test_push", class4.a2)
        return 0
    def fonk4(self):
        self.b2("Running test_pop", class4.a2)
        return 0
    def fonk5(self):
        self.b2("Running test_shift", class4.a2)
        return 0
    def fonk6(self):
        self.b2("Running test_unshift", class4.a2)
        return 0
    def fonk7(self):
        self.b2("Running test_contains", class4.a2)
        return 0
    def fonk8(self):
        self.b2("Running test_remove", class4.a2)
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
def fonk14():
    def fonk15(b1, log_filename):
        b5 = class4(log_filename)
        b5.fonk10(f"Testing class {b1.b9}", class4.a2)
        b6 = class3(b1, b5.log)
        a1 = b6.fonk2()
        b7 = "PASSED" if a1 == 0 else "FAILED"
        b5.fonk10(f"{b1.b9} TEST {b7} with {a1} errors", class4.a3)
        b5.fonk12()
        return a1
    b8 = fonk15(class1, "SingleLinkedListTest.txt")
    b8 += fonk15(class2, "DoubleLinkedListTest.txt")
if b9 = = "__main__":
    fonk14()