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
        while(b5.b2):
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self, key):
        b6 = self.b3
        if b6 != None:
            if b6.b1 = = key:
                self.b7 = b6.b2
                b6 = None
                return
        while b6 != None:
            if b6.b1 = = key:
                break
            b8 = b6
            b6 = b6.b2
        if b6 = = None:
            return
        b8.b2 = b6.b2
        b6 = None
    def fonk5(self):
        b9 = self.b3
        while b9 != None:
            print(b9.b1)
            b9 = b9.b2
def fonk6(b11):
        try:
            for i in range(2, len(b11)+1):
                print("d"+str(i) +" = class1('"+b11[i-1]+"')")
        except(TypeError, ValueError):
            print()
def fonk7(b11):
    b10 = []
    try:
        for i in range(2,len(b11)+1):
            b10.append("d"+str(i))
        for d in range(len(b10)-1):
            print(b10[d]+".b2 = " + b10[d+1])
    except(TypeError, ValueError):
        print()
b11 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
b12 = class2()
b12.b3 = class1("Monday")
b13 = class1('Tuesday')
b14 = class1('Wednesday')
b15 = class1('Thursday')
b16 = class1('Friday')
b17 = class1('Saturday')
b18 = class1('Sunday')
b12.b3.b2 = b13
b13.b2 = b14
b14.b2 = b15
b15.b2 = b16
b16.b2 = b17
b17.b2 = b18
b12.fonk5()
print("*"*40)
b12.fonk3("frargsday")
b12.fonk5()
print("*"*40)
b12.fonk4("frargsday")
b12.fonk5()