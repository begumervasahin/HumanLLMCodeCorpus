import random
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        print(f"Performing b1 b9: b3 = '{self.b1}', Representation='{self.b2}'")
class class2:
    def fonk3(self, b4, b2):
        self.b4 = b4
        self.b2 = b2
    def fonk4(self):
        print(f"Performing b4 b9: b5 = {self.b4}, Representation='{self.b2}'")
class class3:
    def fonk5(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.b8 = None
    def fonk6(self):
        print(f"{self.b6}: {self.b7}")
        b2 = input("Enter your b2: ")
        if b2 in self.b7:
            self.b8 = b2
        else:
            print("Invalid b2.")
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
    if fonk9([b10, b11], "b3 Search"):
        b9 = class1(b11.b8, b10.b8)
        b9.fonk4()
def fonk11():
    if fonk9([b10, b12], "b5 Search"):
        b9 = class2(int(b12.b8), b10.b8)
        b9.fonk4()
def fonk12():
    global b10, b11, b12
    b10 = class3("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
    b11 = class4("b3 to b9")
    b12 = class4("b5 to b9 (0x for hex, 0b for binary)")
    fonk10()
    fonk11()
if b13 = = "__main__":
    fonk12()