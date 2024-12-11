class class1:
    def fonk1(self):
        self.b1 = "generic"
class class2(class1):
    def fonk2(self):
        super().fonk2()
        self.b1 = "adaboost"
b2 = class2()
print(b2.b1)
