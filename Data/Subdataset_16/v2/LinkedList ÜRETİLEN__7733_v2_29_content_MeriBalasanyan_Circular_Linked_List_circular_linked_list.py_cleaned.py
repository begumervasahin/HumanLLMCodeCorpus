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
    def fonk4(self, b3, b4):
        b7 = self.b6
        while True:
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                return b7
            b7 = b7.b2
            if b7 = = self.b6:
                break
        return None
    def fonk5(self):
        if self.b6 is None:
            print("List is empty")
            return
        b7 = self.b6
        while True:
            print(f"Name: {b7.b1.b3}, b4: {b7.b1.b4}, b5: {b7.b1.b5}")
            b7 = b7.b2
            if b7 = = self.b6:
                break
        print("----------")
    def fonk6(self, new_data):
        b8 = class1(new_data)
        if self.b6 is None:
            self.b6 = b8
            b8.b2 = b8
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b8
            b8.b2 = self.b6
    def fonk7(self, prev_name, prev_ID, new_data):
        b8 = class1(new_data)
        b9 = self.fonk4(prev_name, prev_ID)
        if b9 is None:
            print("This student is not in the list")
            return
        b8.b2 = b9.b2
        b9.b2 = b8
    def fonk8(self, b3, b4):
        if self.b6 is None:
            return
        b7 = self.b6
        b10 = None
        while True:
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                if b10 is not None:
                    b10.b2 = b7.b2
                else:
                    while b7.b2 != self.b6:
                        b7 = b7.b2
                    b7.b2 = self.b6.b2
                    self.b6 = self.b6.b2
                return
            b10 = b7
            b7 = b7.b2
            if b7 = = self.b6:
                break
    def fonk9(self):
        if self.b6 is None:
            return
        b10 = None
        b11 = self.b6
        b12 = b11.b2
        while True:
            b12 = b11.b2
            b11.b2 = b10
            b10 = b11
            b11 = b12
            if b11 = = self.b6:
                break
        self.b6.b2 = b10
        self.b6 = b10
    def fonk10(self, new_head_name, new_head_ID):
        b13 = self.fonk4(new_head_name, new_head_ID)
        if b13 is not None:
            self.b6 = b13
def fonk11():
    b14 = class3()
    b15 = class2("Meri", "111", "3.0")
    b16 = class2("John", "112", "3.5")
    b17 = class2("Anna", "113", "3.8")
    b14.fonk6(b15)
    b14.fonk6(b16)
    b14.fonk6(b17)
    print("Original list:")
    b14.fonk5()
    b14.fonk9()
    print("Reversed list:")
    b14.fonk5()
    b18 = class2("Mike", "114", "3.2")
    b14.fonk7("John", "112", b18)
    print("List after appending Mike after John:")
    b14.fonk5()
    b14.fonk8("Anna", "113")
    print("List after deleting Anna:")
    b14.fonk5()
    b14.fonk10("Mike", "114")
    print("List after changing b6 to Mike:")
    b14.fonk5()
if b19 = = "__main__":
    fonk11()