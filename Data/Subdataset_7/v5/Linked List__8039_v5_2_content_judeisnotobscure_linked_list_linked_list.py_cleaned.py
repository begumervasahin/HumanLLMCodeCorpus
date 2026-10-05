class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, data):
        b4 = class1(data)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self, key):
        b6 = self.b3
        if b6 and b6.b1 = = key:
            self.b3 = b6.b2
            b6 = None
            return
        b7 = None
        while b6 and b6.b1 != key:
            b7 = b6
            b6 = b6.b2
        if b6 is None:
            return
        b7.b2 = b6.b2
        b6 = None
    def fonk5(self):
        b6 = self.b3
        while b6:
            print(b6.b1)
            b6 = b6.b2
def fonk6():
    b8 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    b9 = class2()
    for day in b8:
        b9.fonk3(day)
    b9.fonk5()
    print("*" * 40)
    b9.fonk3("frargsday")
    b9.fonk5()
    print("*" * 40)
    b9.fonk4("frargsday")
    b9.fonk5()
if b10 = = "__main__":
    fonk6()