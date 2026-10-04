class class1:
    def fonk1(self):
        self.b1 = "base_model"
class class2(class1):
    def fonk2(self):
        super().fonk2()
        self.b1 = "adaboost"
if b2 = = "__main__":
    b3 = class2()
    print(f"The model type is: {b3.b1}")