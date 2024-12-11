class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self, key):
        b5 = self.b3
        if b5 and b5.b1 = = key:
            self.b3 = b5.b2
            b5 = None
            return
        b6 = None
        while b5 and b5.b1 != key:
            b6 = b5
            b5 = b5.b2
        if b5 is None:
            return
        b6.b2 = b5.b2
        b5 = None
    def fonk5(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2
b7 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
b8 = class2()
b8.b3 = class1("Monday")
b5 = b8.b3
for day in b7[1:]:
    b4 = class1(day)
    b5.b2 = b4
    b5 = b4
b8.fonk5()
print("*" * 40)
b8.fonk3("frargsday")
b8.fonk5()
print("*" * 40)
b8.fonk4("frargsday")
b8.fonk5()