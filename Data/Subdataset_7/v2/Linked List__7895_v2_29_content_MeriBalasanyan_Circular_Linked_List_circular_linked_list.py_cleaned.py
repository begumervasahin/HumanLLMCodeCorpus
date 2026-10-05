class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
class class3:
    def fonk3(self):
        self.b6 = None
    def fonk4(self, b1):
        b7 = self.b6
        while b7.b1 != b1:
            b7 = b7.b2
            if b7 = = self.b6:
                return None
        return b7
    def fonk5(self):
        if self.b6 is None:
            print("List is empty")
            return
        b7 = self.b6
        while True:
            print(f"b3: {b7.b1.b3}, b4: {b7.b1.b4}, b5: {b7.b1.b5}")
            b7 = b7.b2
            if b7 = = self.b6:
                break
        print("----------")
    def fonk6(self, new_data):
        b8 = class2(new_data.b3, new_data.b4, new_data.b5)
        if self.b6 is None:
            b8.b2 = b8
            self.b6 = b8
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b8
            b8.b2 = self.b6
    def fonk7(self, prev_data, new_data):
        b9 = self.fonk4(prev_data)
        if b9 is None:
            print("Previous student not found in the list")
            return
        b8 = class2(new_data.b3, new_data.b4, new_data.b5)
        b8.b2 = b9.b2
        b9.b2 = b8
    def fonk8(self, b3, b4):
        if self.b6 is None:
            print("List is empty")
            return
        b7 = self.b6
        if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = self.b6.b2
            self.b6 = self.b6.b2
            return
        b10 = None
        while b7.b2 != self.b6:
            b10 = b7
            b7 = b7.b2
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                b10.b2 = b7.b2
                return
        if b7.b2 = = self.b6:
            print("class2 not found in the list")
    def fonk9(self):
        if self.b6 is None:
            print("List is empty")
            return
        b10 = None
        b7 = self.b6
        while b7.b2 != self.b6:
            b11 = b7.b2
            b7.b2 = b10
            b10 = b7
            b7 = b11
        b7.b2 = b10
        self.b6.b2 = b7
        self.b6 = b7
    def fonk10(self, new_head):
        b12 = self.fonk4(new_head)
        if b12 is not None:
            self.b6 = b12
def fonk11():
    b13 = class3()
    b14 = class2("meri", "111", "3.0")
    b13.fonk6(b14)
    b13.fonk5()
    b13.fonk9()
    b13.fonk5()
if b15 = = "__main__":
    fonk11()