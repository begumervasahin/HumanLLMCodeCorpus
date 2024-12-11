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
                self.b7 = b6.b2
                b6 = None
                return
        while b6 is not None:
            if b6.b1 = = key:
                break
            b8 = b6
            b6 = b6.b2
        if b6 is None:
            return
        b8.b2 = b6.b2
        b6 = None
    def fonk5(self):
        b9 = self.b3
        while b9 is not None:
            print(b9.b1)
            b9 = b9.b2
def fonk6(lst):
    try:
        for i in range(2, len(lst) + 1):
            print("d" + str(i) + " = class1('" + lst[i - 1] + "')")
    except (TypeError, ValueError):
        print("Usage: fonk6(list)\nArgs:\b10 = [] any list")
def fonk7(lst):
    b11 = []
    try:
        for i in range(2, len(lst) + 1):
            b11.append("d" + str(i))
        for d in range(len(b11) - 1):
            print(b11[d] + ".b2 = " + b11[d + 1])
    except (TypeError, ValueError):
        print("Usage: fonk7(list)\nArgs:\b10 = [] any list")
b12 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
b13 = class2()
b13.b3 = class1("Monday")
b14 = class1('Tuesday')
b15 = class1('Wednesday')
b16 = class1('Thursday')
b17 = class1('Friday')
b18 = class1('Saturday')
b19 = class1('Sunday')
b13.b3.b2 = b14
b14.b2 = b15
b15.b2 = b16
b16.b2 = b17
b17.b2 = b18
b18.b2 = b19
b13.fonk5()
print("*" * 40)
b13.fonk3("frargsday")
b13.fonk5()
print("*" * 40)
b13.fonk4("frargsday")
b13.fonk5()