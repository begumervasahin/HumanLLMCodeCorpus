class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, val):
        self.b4 = class1(val)
        self.b5 = self.b4
    def fonk3(self, val):
        b6 = class1(val)
        self.b5.b2 = b6
        b6.b3 = self.b5
        self.b5 = b6
    def fonk4(self, val, new_val):
        b6 = class1(new_val)
        if self.b5.b1 = = val:
            self.fonk3(new_val)
        elif self.b4.b1 = = val:
            b6.b2 = self.b4.b2
            if b6.b2:
                b6.b2.b3 = b6
            self.b4.b2 = b6
            b6.b3 = self.b4
        else:
            b7 = self.b4
            while b7 and b7.b1 != val:
                b7 = b7.b2
            if b7:
                b6.b2 = b7.b2
                if b6.b2:
                    b6.b2.b3 = b6
                b7.b2 = b6
                b6.b3 = b7
    def fonk5(self, val):
        if self.b4.b1 = = val:
            self.b4 = self.b4.b2
            if self.b4:
                self.b4.b3 = None
        elif self.b5.b1 = = val:
            self.b5 = self.b5.b3
            if self.b5:
                self.b5.b2 = None
        else:
            b7 = self.b4
            while b7 and b7.b1 != val:
                b7 = b7.b2
            if b7:
                b7.b3.b2 = b7.b2
                if b7.b2:
                    b7.b2.b3 = b7.b3
    def fonk6(self):
        b7 = self.b5
        while b7:
            print(b7.b1)
            b7 = b7.b3
    def fonk7(self):
        b7 = self.b4
        while b7:
            print(b7.b1)
            b7 = b7.b2
b8 = class2(10)
b8.fonk3(20)
b8.fonk3(30)
b8.fonk3(40)
b8.fonk5(40)
print("Forward traversal:")
b8.fonk7()
print("Reverse traversal:")
b8.fonk6()