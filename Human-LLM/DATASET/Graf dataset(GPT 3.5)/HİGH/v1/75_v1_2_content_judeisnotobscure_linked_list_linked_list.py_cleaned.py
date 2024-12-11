class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, endData):
        b4 = class1(endData)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self, key):
        b6 = self.b3
        if b6 is not None:
            if b6.b1 = = key:
                self.b3 = b6.b2
                b6 = None
                return
        while b6 is not None:
            if b6.b1 = = key:
                break
            b7 = b6
            b6 = b6.b2
        if b6 is None:
            return
        b7.b2 = b6.b2
        b6 = None
    def fonk5(self):
        b8 = self.b3
        while b8 is not None:
            print(b8.b1)
            b8 = b8.b2
b9 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
b10 = class2()
b10.b3 = class1("Monday")
b11 = class1('Tuesday')
b12 = class1('Wednesday')
b13 = class1('Thursday')
b14 = class1('Friday')
b15 = class1('Saturday')
b16 = class1('Sunday')
b10.b3.b2 = b11
b11.b2 = b12
b12.b2 = b13
b13.b2 = b14
b14.b2 = b15
b15.b2 = b16
b10.fonk5()
print("*"*40)
b10.fonk3("frargsday")
b10.fonk5()
print("*"*40)
b10.fonk4("frargsday")
b10.fonk5()