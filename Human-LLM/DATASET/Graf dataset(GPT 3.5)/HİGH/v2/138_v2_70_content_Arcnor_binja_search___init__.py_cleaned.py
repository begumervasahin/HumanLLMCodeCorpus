class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        print(f"Performing b1 b10: b3 = '{self.b1}', Representation='{self.b2}'")
class class2:
    def fonk3(self, b4, b2):
        self.b4 = b4
        self.b2 = b2
    def fonk4(self):
        print(f"Performing b4 b10: b5 = {self.b4}, Representation='{self.b2}'")
class class3:
    def fonk5(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.b8 = None
    def fonk6(self):
        print(f"{self.b6}: {self.b7}")
        b9 = input("Enter your b9: ")
        if b9 in self.b7:
            self.b8 = b9
        else:
            print("Invalid b9.")
class class4:
    def fonk7(self, b6):
        self.b6 = b6
        self.b8 = None
    def fonk8(self):
        self.b8 = input(f"Enter {self.b6}: ")
def fonk9(fields, title):
    print(title)
    for field in fields:
        field.fonk8()
        if field.b8 is None:
            return False
    return True
def fonk10():
    if fonk9([b11, b12], "b3 Search"):
        b10 = class1(b12.b8, b11.b8)
        b10.fonk4()
def fonk11():
    if fonk9([b11, b13], "b5 Search"):
        b10 = class2(int(b13.b8), b11.b8)
        b10.fonk4()
def fonk12():
    global b11, b12, b13
    b11 = class3("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
    b12 = class4("b3 to b10")
    b13 = class4("b5 to b10 (0x for hex, 0b for binary)")
    fonk10()
    fonk11()
if b14 = = "__main__":
    fonk12()