class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        if self.b1 > 1:
            print("Weee, this is fun!")
        elif self.b1 = = 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")
class class2:
    def fonk3(self):
        self.b2 = class1(1.8)
    def fonk4(self):
        print("Waddle waddle waddle")
    def fonk5(self):
        print("Come on in the water is lovely")
    def fonk6(self):
        print("Quack Quack")
    def fonk7(self):
        self.b2.fonk7()
class class3(class2):
    pass
class class4:
    def fonk8(self):
        self.b3 = self.aviate
    def fonk9(self):
        print("Waddle waddle I waddle too")
    def fonk10(self):
        print("Come on in but it's a bit chilly this far south")
    def fonk11(self):
        print("Are you having a laugh on a penguin?")
    def fonk12(self):
        print("I won the lottery and bought a learjet")
class class5:
    def fonk13(self):
        self.b4 = []
    def fonk14(self, duck: class2) -> None:
        b5 = getattr(duck, "b3", None)
        if callable(b5):
            self.b4.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it is not a " + str(type(duck).b7) + "?")
    def fonk15(self):
        b6 = None
        for duck in self.b4:
            try:
                duck.fonk7()
                raise AttributeError("Testing exception handling in migrate")
            except AttributeError as e:
                print("One duck down")
                b6 = e
        if b6:
            raise b6
def fonk16(duck):
    duck.fonk9()
    duck.fonk10()
    duck.fonk11()
if b7 = = "__main__":
    b8 = class2()
    b8.fonk7()