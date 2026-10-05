class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        print(f"Performing {self.__class__.b12}: b3 = '{self.b1}', Representation='{self.b2}'")
class class2:
    def fonk3(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b6 = None
    def fonk4(self):
        print(f"{self.b4}: {self.b5}")
        b7 = input("Enter your b7: ")
        if b7 in self.b5:
            self.b6 = b7
        else:
            print("Invalid b7.")
class class3:
    def fonk5(self, b4):
        self.b4 = b4
        self.b6 = None
    def fonk6(self):
        self.b6 = input(f"Enter {self.b4}: ")
def fonk7(fields, title):
    print(title)
    for field in fields:
        field.fonk6()
        if field.b6 is None:
            return False
    return True
def fonk8(search_type, query_field, b9, title):
    if fonk7([b9, query_field], title):
        b8 = search_type(query_field.b6, b9.b6)
        b8.fonk2()
def fonk9():
    b9 = class2("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
    b10 = class3("Text to b8")
    b11 = class3("Number to b8 (0x for hex, 0b for binary)")
    fonk8(class1, b10, b9, "Text class1")
    fonk8(class1, b11, b9, "Number class1")
if b12 = = "__main__":
    fonk9()